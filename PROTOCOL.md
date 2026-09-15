# ANK2 Functional Convergence Project — Research Protocol

**Status:** Pre-analysis protocol. Written before data collection.
**Version:** 2.0
**Date:** 2026-09-15

---

## 1. Research Question

Where does the functional evidence for ANK2's ADHD association point within
ANK2's known domain/mechanism architecture, relative to cardiac
(ion-channel / excitation-coupling) and autism (cytoskeletal / synaptic)
mechanisms?

## 2. Hypotheses

- **H1a — Cytoskeletal convergence:** ADHD evidence points mainly to cytoskeletal, spectrin-associated, cell-junction, synaptic functions.
- **H1b — Excitability convergence:** ADHD evidence points mainly to ion-channel, calcium-handling, excitability functions.
- **H1c — Intersectional:** Substantial evidence for both, no clear dominance.
- **H0:** Available evidence does not preferentially point to either axis.

Verdict language only: `supported / partially supported / not supported / evidence insufficient`. Never `proved`.

## 3. Limitation + PPI interpretation rule (read before any analysis)

1. Demontis et al. 2025 provides no public ADHD ANK2 variant coordinates. We do **not** map ADHD variants. ADHD "localization" is inference from indirect evidence only.
2. **PPI rule:** Demontis IP-MS (158 ANK2 interactors, neuronal NPC/ExN) describes ANK2's *normal* neuronal interaction architecture, **not** ADHD-specific disruption. We use it for contextualization only:
   - High confidence: ANK2 gene <-> ADHD (genetics), variant classes = protein-perturbing.
   - Medium confidence: PPI = what ANK2 does in neurons normally.
   - Low confidence (assumption, must be labelled as such): ADHD perturbation acts through that neuronal architecture.
3. Failure to reject H0 = "evidence does not support preferential localization", not "no localization exists".

---

## 4. Repo (minimal, create once)

```text
ANK2-functional-convergence/
├── README.md
├── PROTOCOL.md (this file, frozen)
├── requirements.txt
├── data/raw/          # original downloads, never edit
├── data/processed/    # cleaned csvs
├── data/metadata/     # reference, structures, logs
├── results/tables/
├── results/figures/
└── docs/decisions.md  # every manual choice logged with date
```

`requirements.txt`: `pandas, numpy, matplotlib, requests, jupyter, biopython`

## 5. Inclusion / Exclusion (frozen)

- **ASD:** variant explicitly reported as disease-associated in Kizhner et al. 2025 (PMC12681835) OR SFARI Gene ANK2 entry. Record source. Exclude synonymous, exclude VUS-equivalent.
- **Cardiac:** ClinVar ANK2 + condition contains "Long QT syndrome 4" OR "Ankyrin-B syndrome" OR "ankyrin-B-related cardiac arrhythmia", aggregated classification Pathogenic / Likely Pathogenic, no conflicting Benign/Likely Benign. Log conflicts as excluded.
- **ADHD evidence only (no variants):** gene burden P=2.72e-6 OR=5.55 (Suppl Table 4); Class I + Class II contribution; PPI enrichments actin P=2.77e-39, cell junction P=1.17e-30 (Suppl Table 11); comorbidity driver (ADHD+ASD/ID).
- **Coordinates:** MANE Select transcript confirmed in Step 2. All protein positions -> UniProt Q01484 canonical. Truncations positioned by onset. Duplicates counted once.
- **Domains:** UniProt Q01484 features only. Scheme: membrane-binding (24 ANK repeats) / spectrin-binding (ZU5A-ZU5B-UPA) / death / C-terminal regulatory. Record access date. If InterPro disagrees, note it, keep UniProt for mapping.

## 6. Evidence grades (freeze before Step 9)

| Level | Meaning | Example |
|---|---|---|
| 4 Direct | Variant shown experimentally to alter specific ANK2 interaction/function | R990Q disrupts βII-spectrin binding |
| 3 Strong indirect | Domain/interface experimentally known to mediate relevant function | ZU5/UPA binds βII-spectrin |
| 2 Functional association | PPI/GO/pathway enrichment only | ANK2 network enriched for actin |
| 1 Contextual | Comorbidity / general literature | ADHD+ASD overlap |

Every domain-function claim in Step 9 gets a grade. No grade inflation.

---

## 7. Steps

### Step 1 — Setup (~30 min)
**Goal:** reproducible folders.
**Tools:** Git, GitHub, VS Code.
**Do:** create repo layout from §4, commit PROTOCOL.md, requirements.txt, empty `docs/decisions.md`.
**Output:** GitHub repo + first commit.
**Done when:** `data/raw`, `data/processed`, `results/` exist.

### Step 2 — Reference transcript/protein (~1 hr)
**Goal:** one coordinate system.
**Tools:** Ensembl browser, NCBI RefSeq browser, UniProt website (free).
**Do:** search human ANK2 → record MANE Select transcript ID, genomic coords, CDS length, UniProt Q01484 length, any mismatch. Write to file.
**Output:** `data/metadata/ank2_reference.md`
**Done when:** transcript ID + Q01484 length + access date recorded.

### Step 3 — Domain map (~1-2 hr)
**Goal:** master protein map.
**Tools:** UniProt Q01484 Features viewer (browser), download TSV.
**Do:** copy start/end for ANK repeats, ZU5A, ZU5B, UPA, death, C-terminal, disordered regions, known binding sites.
**Output:** `data/processed/domain_boundaries.csv` with columns `feature,start,end,source,access_date`.
**Done when:** every variant in Steps 5-6 can be assigned or explicitly `unassigned`.

### Step 4 — Structure coverage (~1 hr)
**Goal:** know what is experimental vs predicted.
**Tools:** rcsb.org search "Q01484 OR ankyrin-B", alphafold.ebi.ac.uk Q01484 (browser download only).
**Do:** list PDB IDs + residues covered + method/resolution; download AlphaFold PDB for Q01484; label regions experimental / predicted-high / predicted-low / disordered.
**Output:** `data/metadata/ank2_structures.csv` + `structure_coverage.csv`, structure file in `data/raw/`.
**Done when:** you can state in one sentence which domains lack experimental structure.

### Step 5 — ASD variants (~2-3 hr, manual)
**Goal:** curated ASD set.
**Tools:** Kizhner PDF, SFARI Gene website, spreadsheet/Python.
**Do:** extract HGVS_c/p, position, type, source. Do not infer domains yet.
**Output:** `data/raw/asd_variants_raw.csv` → `data/processed/asd_variants.csv`
**Done when:** each row has `hgvs_p,position,variant_type,source`.

### Step 6 — Cardiac variants (~2 hr)
**Goal:** high-confidence cardiac set.
**Tools:** ClinVar website — search `ANK2[gene]`, filter P/LP, download CSV (no API needed).
**Do:** filter by condition strings in §5, apply conflict rule, log excluded.
**Output:** `data/processed/cardiac_variants.csv` + exclusion log in `docs/decisions.md`.
**Done when:** N included + N excluded both recorded.

### Step 7 — Map + tally ASD vs cardiac (~3-4 hr)
**Goal:** the quantitative core.
**Tools:** Python pandas + matplotlib, Jupyter.
**Do:** normalize positions to Q01484, assign domain via Step 3 table (truncation = onset), counts + % per domain, one contingency table. Fisher's exact only if counts allow, otherwise descriptive + permutation optional. One lollipop plot with matplotlib.
**Output:** `results/tables/variant_domain_assignments.csv`, `domain_distribution.csv`, `results/figures/fig2_lollipop.png`.
**Done when:** you can state ASD vs cardiac domain pattern in 2 sentences with numbers.

### Step 8 — ADHD evidence table (~1-2 hr)
**Goal:** machine-readable Demontis summary, no prose re-interpretation.
**Tools:** Demontis main text + Suppl Tables 4, 11 (already have).
**Do:** one row per evidence item: `claim, value, type [genetic/variant-class/PPI/phenotype], source_table, confidence [high/med/low]`.
**Output:** `data/processed/adhd_evidence_summary.csv` + `docs/adhd_evidence_summary.md`.
**Done when:** 8 rows minimum covering §5 ADHD items.

### Step 9 — PPI interactor list + graded domain mapping (~3-4 hr)
**Goal:** ground Step 10 in genes, not just p-values.
**Tools:** Demontis Suppl PPI Tables 1-4 (xlsx), g:Profiler web (free, no install).
**Do:**
  a. Extract 158 interactors: `gene, cell_type [NPC/ExN], FC, FDR` → `data/processed/ank2_adhd_ppi.csv`.
  b. Paste gene list into g:Profiler, record top GO/Reactome/SynGO terms.
  c. For each enriched function, look up which ANK2 region binds relevant interactors (literature/UniProt). Assign domain + evidence grade from §6. Never assign SBD from "actin" alone without an interaction source.
**Output:** `ank2_adhd_ppi.csv`, `ppi_functional_annotations.csv`, `results/tables/adhd_domain_mechanistic_mapping.csv` with `function,candidate_region,source,grade`.
**Done when:** every mapping row has a source + grade 1-4.

### Step 10 — Interpret + write (~3-4 hr)
**Goal:** verdict without overclaim.
**Tools:** Markdown.
**Do:** for H1a/H1b/H1c/H0 write `supports / against / grade / uncertainty / verdict`. Use allowed verbs: PPI claims → "consistent with"; variant claims → "shows". Banned for PPI: "disrupts, mediates, proves".
**Output:** `results/hypothesis_assessment.md`, final `README.md` (Background, RQ, Methods, Results, Limitations, Conclusion), figures: Fig1 architecture, Fig2 lollipop, Fig3 PPI network (simple), Fig4 convergence schematic.
**Done when:** limitation §3 appears verbatim in README Limitations.

---

## 8. What this does not do
- No ADHD variant positions, no ADHD-vs-cardiac p-value.
- No ΔΔG / FoldX / Rosetta (skip — low return for 2400aa disordered protein).
- No custom enrichment code required — g:Profiler web is sufficient.

## 9. Stretch goals (only after Steps 1-10 done)
1. Cardiac ANK2 interactor contrast (neuronal vs cardiac architecture).
2. Control scaffold (e.g. ANK3/SPTBN1) to test enrichment specificity.
3. ChimeraX figure of 1-2 representative ASD/cardiac variants in resolved regions.

## 10. Stack
Browser: Ensembl, UniProt, RCSB PDB, AlphaFold DB, ClinVar, SFARI, g:Profiler. Local: Python pandas/matplotlib, Jupyter, ChimeraX, Git/GitHub.
