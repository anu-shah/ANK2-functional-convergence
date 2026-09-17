"""Reproduce Step 7 analysis: domain tallies, Fisher tests, Bonferroni, lollipop plot.

Run: python scripts/analysis.py
Writes: results/tables/step7_enrichment_audit.csv, results/figures/fig2_lollipop.png
"""
import csv
import math
from collections import Counter
from pathlib import Path
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
ASSIGN = ROOT / "data/processed/variant_domain_assignments.csv"
BOUNDS = ROOT / "data/processed/domain_boundaries.csv"
AUDIT = ROOT / "results/tables/step7_enrichment_audit.csv"
FIG = ROOT / "results/figures/fig2_lollipop.png"

rows = list(csv.DictReader(open(ASSIGN)))
counts = {g: Counter(r["broad_category"] for r in rows if r["group"] == g) for g in ("ASD", "Cardiac")}
CATS = ["ANK_repeats", "ZU5", "UPA", "Death_domain", "Repeat_rich", "Disordered", "Other", "Unassigned"]

b = list(csv.DictReader(open(BOUNDS)))
def span(start_pred, end_pred):
    s = [int(r["start"]) for r in b if start_pred(r)]
    e = [int(r["end"]) for r in b if end_pred(r)]
    return max(e) - min(s) + 1
lens = {
    "ANK_repeats": span(lambda r: r["feature"].startswith("ANK "),
                        lambda r: r["feature"].startswith("ANK ")),
    "ZU5": span(lambda r: r["feature"].startswith("ZU5 "),
                lambda r: r["feature"].startswith("ZU5 ")),
    "UPA": span(lambda r: r["feature"] == "UPA domain",
                lambda r: r["feature"] == "UPA domain"),
    "Disordered": sum(int(r["end"]) - int(r["start"]) + 1 for r in b
                      if r["feature_type"] == "Region" and r["feature"].startswith("Disordered")),
}
for c in ("Death_domain", "Repeat_rich", "Other", "Unassigned"):
    lens[c] = None

N_ASD, N_CAR = sum(counts["ASD"].values()), sum(counts["Cardiac"].values())

def fisher(cat):
    a, c = counts["ASD"].get(cat, 0), counts["Cardiac"].get(cat, 0)
    if a + c == 0:
        return {"category": cat, "asd": 0, "cardiac": 0, "or_raw": math.nan,
                "p_two_sided": math.nan, "or_haldane": math.nan, "ci_lo": math.nan,
                "ci_hi": math.nan, "asd_rate_per_residue": math.nan,
                "cardiac_rate_per_residue": math.nan, "status": "none"}
    b_, d = N_ASD - a, N_CAR - c
    odds, p = stats.fisher_exact([[a, b_], [c, d]], alternative="two-sided")
    # Haldane 0.5 correction on log-odds scale for the CI (kept in the reported CI only)
    ha, hb, hc, hd = a + 0.5, b_ + 0.5, c + 0.5, d + 0.5
    se = math.sqrt(sum(1 / x for x in (ha, hb, hc, hd)))
    lor = math.log((ha * hd) / (hb * hc))
    scale = lens.get(cat)
    return {
        "category": cat, "asd": a, "cardiac": c, "or_raw": odds, "p_two_sided": p,
        "or_haldane": odds, "ci_lo": math.exp(lor - 1.96 * se), "ci_hi": math.exp(lor + 1.96 * se),
        "asd_rate_per_residue": a / scale if scale else math.nan,
        "cardiac_rate_per_residue": c / scale if scale else math.nan,
        "status": "tested",
    }

audit_df = pd.DataFrame([fisher(c) for c in CATS])
audit_df.to_csv(AUDIT, index=False)

tested = audit_df[audit_df["status"] == "tested"]
n = len(tested)
alpha = 0.05 / n
sig = tested[tested["p_two_sided"] < alpha]
print(f"{len(tested)} tested categories, Bonferroni alpha = {alpha:.3f}")
for _, r in tested.iterrows():
    mark = " *sig" if r["p_two_sided"] < alpha else ""
    print(f"  {r['category']:<10} {int(r['asd'])} vs {int(r['cardiac'])}  "
          f"p={r['p_two_sided']:.4f}  OR={r['or_raw']}  CI[{r['ci_lo']:.2f},{r['ci_hi']:.2f}]{mark}")
print("  -> no category survives Bonferroni" if sig.empty else "  -> " + ", ".join(sig["category"]))

fig, ax = plt.subplots(figsize=(12, 5))
colors = {"ANK_repeats": "#4C72B0", "ZU5": "#DD8452", "UPA": "#55A868", "Disordered": "#C44E52", "Unassigned": "#8C8C8C"}
for r in rows:
    if not r["protein_position_start"]:
        continue
    cat = r["broad_category"]
    pos = int(r["protein_position_start"])
    ax.plot([pos, pos], [0, 0.9], color=colors.get(cat, "#333"), lw=0.8, alpha=0.6)
    ax.scatter([pos], [0.9], color=colors.get(cat, "#333"), s=40, zorder=3)
    ax.annotate(r["variant_id"], (pos, 0.9), textcoords="offset points", xytext=(0, 6),
                rotation=45, fontsize=6, ha="center")
for r in b:
    if r["feature_type"] in ("Repeat", "Domain") and r["feature"].split(";")[0].strip() in (
            "ANK 1", "ZU5 1", "Death 1", "Death 2", "Repeat A"):
        ax.axvspan(int(r["start"]), int(r["end"]), alpha=0.08, color="#999")
ax.set_xlim(0, 3957)
ax.set_ylim(-0.05, 1.0)
ax.set_yticks([])
ax.set_xlabel("Canonical residue (UniProt Q01484)")
ax.set_title("Curated ASD + cardiac ANK2 variants by domain")
fig.tight_layout()
fig.savefig(FIG, dpi=200)
print("written:", AUDIT.name, FIG.name)