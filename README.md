# ANK2 Functional Convergence

**Where does the functional evidence for ANK2's ADHD association localize within ANK2's known domain/mechanism architecture, relative to cardiac (ion-channel / excitation-coupling) and autism (cytoskeletal / synaptic) mechanisms?**

Protocol: `PROTOCOL.md` v2.0 (frozen 2026-09-15). Companion evidence: `docs/final_synthesis.md`, `results/tables/final_evidence_matrix.csv`.

## Background

ANK2 (ankyrin-2, UniProt Q01484, 3957 residues) is a scaffolding protein with well-characterized cardiac and neuronal roles. Rare ANK2 variation has been implicated in both autism spectrum disorder (ASD) and ADHD, although the available ADHD evidence in this project is gene-level rather than coordinate-resolved. In the Demontis et al. 2025 ADHD rare-variant exome study, ANK2 is an exome-wide-significant ADHD risk gene and also carries ASD/NDD risk-gene flags, making it a natural probe for whether a gene's ADHD mechanism aligns with its cardiac (excitability) or autism (cytoskeletal/synaptic) biology.

## Research question

Does the functional evidence for ANK2's ADHD association localize to an ANK2 domain or mechanism, and if so, does it resemble the cardiac (ion-channel / excitation-coupling) axis, the autism (cytoskeletal / synaptic) axis, both, or neither?

## Methods (Steps 1–10 of PROTOCOL.md)

- **Step 1 — Setup:** reproducible repo layout (folders, PROTOCOL.md, requirements.txt, docs/decisions.md); first commit.
- **Step 2 — Reference transcript/protein:** MANE Select transcript confirmed (NM_001148.6); canonical UniProt Q01484 (3957 residues) established as coordinate system → `data/metadata/ank2_reference.md`.
- **Step 3 — Domain map:** UniProt Q01484 features (ANK repeats 1–24, ZU5 1/2, UPA, Death domains, Repeat-rich, Disordered regions), cross-checked against InterPro/Pfam; 59/59 rows verified against live UniProt (2026-09-16), with boundary-confidence caveats documented in `docs/decisions.md`.
- **Step 4 — Structure coverage:** RCSB PDB (10/10 verified) and AlphaFold DB (isoform-only models; no canonical Q01484 model) → `data/metadata/structure_coverage.csv`.
- **Step 5 — ASD variants:** 11 curated variants from verified primary literature (Chirasani 2025 JBC, Zhao 2025, Guissart 2023, Morais 2023, Garotti 2025); 4 transcription errors corrected and logged.
- **Step 6 — Cardiac variants:** 9 curated ClinVar P/LP variants (6 Pathogenic, 3 Likely Pathogenic; no conflicts; As 3-star where criteria met); verified against live ClinVar (2026-09-16).
- **Step 7 — Map + tally:** variants assigned to domains (truncation = onset); counts/%; Fisher's exact as an exploratory test with OR-with-CI and Bonferroni correction; lollipop plot.
- **Step 8 — ADHD evidence:** 12-row machine-readable table extracted from Demontis et al. 2025 main text + Supplementary Tables 4/11 + PPI Table 8; verified field-by-field against the actual files (2026-09-16).
- **Step 9 — PPI → domain mapping:** 158-member ANK2 union; 2/158 mapped (SPTBN1 → 966–1125 within ZU5 1; L1CAM → ANK repeats 11–14, repeat-level only); 156 not_mappable.
- **Step 10 — Interpretation:** hypothesis verdicts without overclaim (see `results/hypothesis_assessment.md` and `docs/final_synthesis.md`).

## Results

- **ADHD genetic (gene-level):** ANK2 exome-wide-significant ADHD burden — P(final) = 2.273e-6 (main text 2.72e-6), OR(combined class I) = 5.55, pLI = 1.0. Class I: 11 cases / 12 controls (P = 1.204e-4); Class II: 3 cases / 0 controls (P = 2.858e-3). ASD_FDR0.05 = 1; NDD_FDR0.05 = 1. 7 top-20 risk genes overlap the DisGeNET Channelopathies set (corrected P = 2.43e-4; ANK2 among the 4 overlapping genes).
- **ADHD PPI (network-level):** ANK2_Union (158 genes) enriched for actin cytoskeleton (P = 2.77e-39), cell junctions (P = 1.17e-30), synapse (P = 1.52e-29), actin binding (P = 6.79e-28); overlap with ASD/DD rare-variant risk genes (ASD KS P = 7.926e-7; DD P = 1e-15).
- **ASD variant localization:** 6/11 in the ankyrin-repeat array, 4/11 in ZU5 1, 1/11 UPA (exploratory Fisher ANK-vs-non-ANK P = 0.0141; does not survive Bonferroni across 5 tested categories — α = 0.010; rate-per-residue density is highest in ZU5 1, not ANK repeats — reported, not over-claimed).
- **Cardiac variant localization:** sparse — ZU5 1 (n=1), UPA (n=1), Disordered (n=2), 5/9 unassigned (feature map does not cover those residues; not retrospectively assigned). 7/9 are nonsense, frameshift, or splice-site variants (3 nonsense, 3 frameshift, 1 splice-site).
- **Within-ANK2 PPI localization:** 2/158 interactors (SPTBN1, L1CAM). **No ADHD variant has coordinates; therefore no ADHD domain distribution exists.**

## Limitations

Protocol §3 limitation + PPI interpretation rule (verbatim):

1. Demontis et al. 2025 provides no public ADHD ANK2 variant coordinates. We do **not** map ADHD variants. ADHD "localization" is inference from indirect evidence only.
2. **PPI rule:** Demontis IP-MS (158 ANK2 interactors, neuronal NPC/ExN) describes ANK2's *normal* neuronal interaction architecture, **not** ADHD-specific disruption. We use it for contextualization only:
   - High confidence: ANK2 gene <-> ADHD (genetics), variant classes = protein-perturbing.
   - Medium confidence: PPI = what ANK2 does in neurons normally.
   - Low confidence (assumption, must be labelled as such): ADHD perturbation acts through that neuronal architecture.
3. Failure to reject H0 = "evidence does not support preferential localization", not "no localization exists".

Additional project limitations: no individual ADHD ANK2 variant coordinates (ADHD evidence is gene-level only); PPI evidence is network-level (2/158 members localize within ANK2); Step-7 ASD/cardiac samples are small (11 and 9); 5/9 cardiac variants unassigned due to incomplete feature coverage; the Step-7 Fisher result is exploratory and sensitive to coding and sample; the ANK2 union derives from published IP-MS, not a new experiment; missing structural coverage does not imply disorder.

Domain-boundary cross-validation note (2026-09-16): UniProt Q01484 boundaries were cross-checked against live InterPro/Pfam. ZU5 1/2 and Death 2 match InterPro exactly; three callouts remain — (1) the UPA region is UniProt 1289–1423 vs InterPro/Pfam UPA domain 1324–1453 (shared overlap 1324–1423; affects no assignment); (2) UniProt "Death 1" (1450–1535) has no Pfam/InterPro death-domain signature (no variant assigned to it) — **boundary is UniProt-only, lower confidence than other domains**; (3) the terminal ankyrin repeat ANK 24 (793–822) is covered only by ankyrin superfamily/family signatures, not a Pfam single-repeat fragment (Glu819Lys/Ile807Met remain ANK_repeats) — **repeat-24 edge is not independently corroborated, treat as lower confidence than ANK 1–23**. Domains therefore follow UniProt; the three boundary caveats above are approximate.

## Conclusion

Within this curated dataset, the ADHD evidence for ANK2 is **gene-level and PPI-network-level only**; it does **not** localize to a specific ANK2 domain or residue (no ADHD variant-coordinate dataset exists; only 2/158 interactions carry within-ANK2 localization). The autism axis is visible at the variant level (repeat-array concentration, exploratory; ZU5-1 secondary cluster) and the interactome level (actin/junction/synapse/NDD enrichment). The cardiac axis is visible as sparse cardiac-domain variant localization and gene-set-level channelopathy enrichment, but no ANK2 domain is tied to neuronal excitability in this dataset. **The data do not establish an intersectional mechanism or an ADHD-specific domain within ANK2.** Any such localization would exceed the evidence.

## Status / layout

- `data/raw/` — original downloads (unmodified; four Step-5 transcription corrections logged in `docs/decisions.md`)
- `data/processed/`, `data/metadata/` — cleaned and reference files
- `results/tables/`, `results/figures/` — tables (incl. `final_evidence_matrix.csv`, `step7_enrichment_audit.csv`) and figures
- `docs/` — `final_synthesis.md`, `adhd_evidence_summary.md`, `ppi_localization_summary.md`, `decisions.md`