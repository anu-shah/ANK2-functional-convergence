# Hypothesis assessment (Step 10)

Access date: 2026-09-16. Protocol: PROTOCOL.md v2.0, Step 10.
Verdict categories (PROTOCOL §2): `supported / partially supported / not supported / evidence insufficient`. Never `proved`. PPI-derived claims use "consistent with"; variant claims use "shows". Companion synthesis: `docs/final_synthesis.md`; matrix: `results/tables/final_evidence_matrix.csv`.

---

## H1a — Cytoskeletal convergence (ADHD evidence points mainly to cytoskeletal, spectrin-associated, cell-junction, synaptic functions)

**Evidence:**
- ANK2_Union interactome enriched for actin cytoskeleton (GO:0015629 corrected P = 2.77e-39), cell junctions (GO:0030054 P = 1.17e-30), actin binding (GO:0003779 P = 6.79e-28), synapse (GO:0045202 P = 1.52e-29) — gene-set enrichment, PPI-derived, reported as "consistent with" a network-level cytoskeletal/synaptic composition.
- Curated ASD variants (6/11) concentrate in the ankyrin-repeat array (SPTBN1/L1/NrCAM-interacting sites), with a secondary ZU5-1 cluster (4/11). Exploratory Fisher ANK-vs-non-ANK P = 0.0141; OR CI [1.05, 479.96]; does not survive Bonferroni across 5 tested categories (α = 0.010). Rate-per-residue density is highest in ZU5 1 (0.0119/aa), not the repeat array (0.0076/aa).
- Only 2/158 interactors localize within ANK2 (SPTBN1 → 966–1125 within ZU5 1, high; L1CAM → ANK repeats 11–14, repeat-level, medium).

**Against / uncertainty:** the ADHD-specific signal is gene-level (P = 2.273e-6) with no ADHD variant coordinates; network enrichment describes interactor composition, not ANK2 domain function; the ASD repeat-array result is exploratory and not multiple-testing-robust.

**Grade:** Supports (partial) — strong network-level and ASD-variant-level consistency with a cytoskeletal/synaptic axis, but no ADHD-specific within-ANK2 domain localization.

**Verdict: partially supported.**

---

## H1b — Excitability convergence (ADHD evidence points mainly to ion-channel, calcium-handling, excitability functions)

**Evidence:**
- Channelopathy gene-set enrichment among top-20 ADHD risk genes: 4/55 overlap (UBE2S; KCNA2; ANK2; CACNA1D), corrected P = 2.43e-4 — gene-set level.
- Cardiac ANK2 variants (9 ClinVar P/LP) localize sparsely to ZU5 1 (n=1), UPA (n=1), Disordered (n=2); 5/9 unassigned due to incomplete feature coverage (not retrospectively assigned); 7/9 truncation-type consistent with cardiac ankyrin-B loss-of-function from the literature.

**Against / uncertainty:** no ANK2 domain is tied to neuronal excitability in this dataset; channelopathy overlap is gene-set-level, not ANK2-specific; cardiac domain localizations should not be extrapolated to ADHD; the iPSYCH ADHD enrichment involves ion-channel risk genes at the gene-set level only.

**Grade:** Limited — gene-set-level consistency with an excitability axis; no within-ANK2 domain evidence.

**Verdict: evidence insufficient.**

---

## H1c — Intersectional (substantial evidence for both, no clear dominance)

**Evidence:** no curated observation in this dataset connects both axes (cytoskeletal/synaptic and excitability/channel) to a shared ANK2 domain or residue.

**Against / uncertainty:** no intersectional hypothesis test was performed; absence of evidence is a limitation, not evidence against such a mechanism.

**Grade:** Untestable with current data.

**Verdict: evidence insufficient (cannot adequately test).**

---

## H0 — No preferential localization (available evidence does not preferentially point to either axis)

**Evidence for H0:** the ADHD signal is gene-level with no variant coordinates; PPI localization is restricted to 2/158 interactors; ASD repeat-array enrichment is exploratory and not multiple-testing-robust; cardiac localizations are sparse with a large unassigned fraction.

**Against:** gene-set- and network-level enrichments (cytoskeletal/synaptic and channelopathy) do point in preferential directions, but not at ADHD-specific domain resolution.

**Grade:** For the ADHD signal specifically, data do not distinguish H0 from H1a/H1b. For the ASD variant set, the exploratory Fisher result is consistent with (not proof of) preferential repeat-array localization.

**Verdict: evidence does not distinguish (consistent with the protocol rule: failure to reject H0 = "evidence does not support preferential localization", not "no localization exists").**

---

## Summary

| Hypothesis | Verdict | Basis |
|---|---|---|
| H1a Cytoskeletal convergence | Partially supported | Interactome actin/junction/synapse enrichments + ASD variant distribution; network/ASD-variant level only |
| H1b Excitability convergence | Evidence insufficient | Gene-set-level channelopathy overlap; no ANK2 neuronal-excitability domain evidence |
| H1c Intersectional | Evidence insufficient | No shared-domain observation; untestable |
| H0 No preferential localization | Evidence does not distinguish | Gene-level ADHD signal; 2/158 within-ANK2 PPI localization |

Central limitation: **localization of the ADHD signal itself is not possible** — no ADHD ANK2 variant coordinates exist, and within-ANK2 PPI localization is limited to SPTBN1 (ZU5 1) and L1CAM (ANK 11–14).