# ANK2 ADHD Evidence Synthesis — Final Step (Step 10)

Access date: 2026-09-16
Project: ADHD_Project (protocol v2.0)
Companion file: `results/tables/final_evidence_matrix.csv`

---

## 1. Research question

**Where does the functional evidence for ANK2's ADHD association localize within ANK2's known domain/mechanism architecture, relative to the well-characterized cardiac (ion-channel / excitation-coupling) and autism (cytoskeletal / synaptic) mechanisms?**

The answer must keep five layers distinct: (1) direct observations from the curated datasets, (2) statistical results, (3) functional/network evidence, (4) interpretation, and (5) limitations. An association must not be turned into causation.

**Headline answer (detailed in Section 16):** Within this curated dataset, the ADHD evidence for ANK2 is gene-level and network-level. It does not localize to a specific ANK2 domain or residue. The ASD and cardiac variant sets do localize to domains (ankyrin repeats / ZU5-1 and sparse ZU5-1/UPA/C-terminal sites, respectively), but the ADHD signal itself has no curated variant-coordinate dataset, so no residue-level ADHD localization claim is possible. The PPI evidence is primarily network-level: only 2 of 158 ANK2_Union members (SPTBN1, L1CAM) carry explicit ANK2 localization evidence.

## 2. Analytical scope

- Inputs: Steps 3–9 outputs — `domain_boundaries.csv` (Step 3), `ank2_structures.csv`/`structure_coverage.csv` (Step 4), `asd_variants.csv` (Step 5), `cardiac_variants.csv` (Step 6), `variant_domain_assignments.csv`/`domain_distribution.csv` (Step 7), `adhd_evidence_summary.csv` (Step 8), `ank2_ppi_interactors.csv`/`ank2_ppi_domain_assignments.csv`/`ank2_ppi_domain_distribution.csv` (Step 9); plus `docs/decisions.md` and the two prior Step-8/9 markdown reports.
- No new variants or evidence were added. No exploratory analyses beyond the pre-specified steps were performed.
- The only domain-localization hypothesis test in the project remains the exploratory Step-7 Fisher test (Section 4). No additional tests, odds ratios, p-values, enrichment statistics, or machine-learning classifications were computed.
- PROTOCOL.md was not modified.

## 3. Reference architecture

Canonical ANK2 (UniProt Q01484; isoform Q01484-4, 3957 residues) feature map (Step 3, `domain_boundaries.csv`):

- **ANK repeats 1–24** (ANK 1: 30–62 … ANK 24: 793–822): membrane-binding module; repeat-level sites relevant here are ANK 11 (364–393), ANK 15 (496–525), ANK 24 (793–822). *Lower-confidence note: ANK 24 (793–822) is only superfamily-covered in InterPro, not resolved to the individual-repeat level like ANK 1–23; treat its boundary as lower confidence.*
- **ZU5 1 (968–1156)** and **ZU5 2 (1158–1304)**: ZU5-1 is consistent with mediating the beta-spectrin interaction; the explicit UniProt interaction interval with SPTBN1 is **966–1125**, which lies within ZU5 1.
- **UPA region (1289–1423)**.
- **Death domains**: Death 1 (1450–1535), Death 2 (3569–3653); **Repeat-rich region (1806–1983)** with approximate Repeat-A tandem repeats. *Lower-confidence note: Death 1 (1450–1535) has no Pfam/InterPro death-domain corroboration and is UniProt-only; treat its boundary as lower confidence.*
- Multiple **Disordered regions** (1–34, 1457–1486, 1670–2137, 2197–2411, 2430–2484, 2507–2586, 2604–2852, 2864–2904, 2923–2951, 2987–3016, 3069–3099, 3136–3462, 3777–3858).
- Structural coverage (Step 4) is partial and experimental structure exists mainly for the ankyrin-repeat array (28–873), ZU5–ZU5–UPA–DD (951–1568), the LIR motif (1588–1614), and the Death-domain region (1499–1570). No full-length experimental structure exists; no canonical-Q01484 AlphaFold model was identified (isoform-specific AF models do not map to canonical residues). Missing structure does not imply disorder.

## 4. ASD localization

**Dataset (Step 7, `variant_domain_assignments.csv`; n = 11 curated ASD variants):**

| Broad feature class | Count | % of 11 |
|---|---|---|
| ANK repeats | 6 | 54.5 |
| ZU5 | 4 | 36.4 |
| UPA | 1 | 9.1 |
| Death domain / Repeat-rich / Disordered / Other / Unassigned | 0 | 0.0 |

All 11 variants were assigned. Important individual locations:

- **ANK repeat array (6):** ANK 2 (p.(Asn63_Lys95del), splice-induced in-frame deletion), ANK 11 (Ala368Gly — maternally inherited, consistent with disrupting NrCAM binding; Ala373Val — maternally inherited, increased NrCAM binding affinity ~1.7×WT, p=0.02), ANK 15 (Ala525Val), ANK 24 (Ile807Met de novo; Glu819Lys maternal).
- **ZU5 1 (4):** Arg977Gln (maternally inherited; consistent with disrupting β2-spectrin binding; ZU5A subdomain; reduced stability), Arg987Trp (familial; high-functioning ASD), Arg1003Ter (de novo; ASD + epilepsy), Arg1138Ter (de novo; ASD + epilepsy).
- **UPA (1):** Pro1380Arg (de novo; UPA region per paper; not impaired for beta2-spectrin binding; reduced stability ~60% WT).

**Statistical result (Step 7, exploratory only):** ANK repeats vs non-ANK broad class, ASD 6/5 vs Cardiac 0/9 — two-sided Fisher exact P = 0.0141, one-sided P = 0.0119, OR = Inf (zero cell; Haldane-0.5-corrected CI [1.05, 479.96]). Across the 5 tested categories the Bonferroni-corrected α = 0.010, so the ANK-repeats P = 0.0141 does **not** survive multiple-testing correction and is not reported as significant here; it is presented only as an exploratory result with its caveats and is **not** proof of ASD-specific localization.

**Interpretation:** Within this curated dataset, the ASD variants concentrate in the ankyrin-repeat array and, secondarily, in ZU5 1, overlapping known spectrin- and L1/NrCAM-interaction surfaces. The source literature (Chirasani et al. 2025 JBC; Zhao et al. 2025; Morais et al. 2023; Guissart et al. 2023; Garotti et al. 2025) already supports functional effects for several of these sites. The Fisher result is consistent with a repeat-array concentration but is exploratory and small-sample.

## 5. Cardiac localization

**Dataset (Step 7; n = 9 curated ClinVar P/LP cardiac variants):**

| Feature class | Count | % of 9 |
|---|---|---|
| ZU5 | 1 | 11.1 |
| UPA | 1 | 11.1 |
| Disordered | 2 | 22.2 |
| ANK repeats | 0 | 0.0 |
| **Unassigned** | **5** | **55.6** |

Assigned variants: **ZU5 1** — Glu1091fs (1091); **UPA** — Ala1405fs (1405); **Disordered** — Gln3076Ter (3076) and Asp3081fs (3081).

Unassigned (5): Glu3525Ter (3525), Ser3713Ala (3713), Arg3113Ter (3113), Lys1631fs (1631) — no overlapping Step-3 feature; plus splice c.1485+1G>A with no curated protein position (position not inferred).

**Reason for unassigned status:** the Step-3 feature map does not cover all canonical residues. The cardiac dataset therefore contains a substantial fraction of unassigned variants; those variants are **not** retrospectively assigned to any domain.

**Important locations:** Seven of nine variants were nonsense, frameshift, or splice-site variants: 3 nonsense, 3 frameshift, and 1 splice-site variant, with onset positions spanning UPA (1405) through ZU5 1 (1091) and the C-terminal tail (1631–3713). The known cardiac role of ankyrin-B in ion-channel/excitation-coupling biology comes from the source literature, not from new experiments here. This cardiac pattern is not, by itself, evidence of an ANK2 neuronal excitability mechanism and is not ADHD evidence.

## 6. ADHD genetic evidence

From Step 8 (`adhd_evidence_summary.csv`). There is **no curated individual ADHD ANK2 variant-coordinate dataset**; the ADHD evidence is summarized across four categories:

**Genetic (gene-level):**
- ANK2 is an exome-wide-significant ADHD rare-variant risk gene: P(final) combined class I+II gene burden = **2.273e-6** (main text reports 2.72e-6; exact ST4 value preserved), OR (combined class I) = **5.55**, pLI = **1.0** (AD-01).
- ANK2 is a known ASD/NDD rare-variant risk gene: ASD_FDR0.05 = 1 and NDD_FDR0.05 = 1 in the Demontis ST4 flags (AD-04).
- Top-20 ADHD risk genes are enriched for the DisGeNET **Channelopathies** set: 4/55 genes (UBE2S; KCNA2; ANK2; CACNA1D), raw P = 2.40e-7, corrected P = **2.43e-4** (AD-07).

**Variant-class:**
- Class I (rPTV) burden: **11** iPSYCH ADHD cases / **12** combined controls; P(combined c1) = **1.204e-4**; OR = **5.55** (AD-02).
- Class II (rModerateDMV) burden: **3** cases / **0** combined controls; P(combined c2) = **2.858e-3**; OR = Inf (AD-03).
- This mixed class I + class II architecture is described as distinct from MAP1A and ANO8 (class I only).

**Phenotype:**
- Among ANK2 class I carriers (n = 11, Supp Fig 5): 1 control; **7 ADHD-only**; **2 ADHD+ID**; **1 ADHD+ASD+SZ+ID** (AD-06).
- Main-text Discussion: the signal was "driven mainly" by ADHD with co-occurring ASD/ID (qualitative, AD-05).

**PPI (summarized in Section 7).**

**Constraint:** because no ADHD ANK2 variant-coordinate dataset exists here, **no ADHD variant-domain distribution was created** and **no ADHD variant was placed on ANK2**. The ADHD signal is **not** residue-level localized.

## 7. ADHD PPI/network evidence

From Step 8 (network-level, published IP-MS–derived network from Table S2 of ref 27):

- **Actin cytoskeleton** GO:0015629: 51 overlapping genes; corrected P = **2.77e-39** (AD-08).
- **Cell junction** GO:0030054: 78 overlapping genes; corrected P = **1.17e-30** (AD-09).
- **Synapse / synaptic annotations:** 70/158 (44.30%) of the union map to SynGO; synapse GO:0045202 corrected P = **1.52e-29** (AD-10). Additional SynGO enrichments include presynapse P=1.95e-14 and postsynapse P=1.35e-25.
- **Actin binding** GO:0003779: 40 overlapping genes; corrected P = **6.79e-28** (AD-12); actin filament binding GO:0051015 corrected P = 1.66e-27.
- **ASD/DD rare-variant overlap in ANK2_Union:** ASD KS P = **7.926e-7**, FDR = 1.902e-6; DD P = **1e-15** (AD-11).

The available evidence is consistent with an ANK2 interactome enriched in actin/cytoskeletal, junction, and synaptic biology, with overlap of NDD-associated rare-variant risk genes. These enrichments describe the composition of the 158-gene network and do not, by themselves, localize any function to a specific ANK2 domain.

## 8. ADHD PPI localization

From Step 9. The ANK2_Union is **158 genes** (NPC 76, ExN 108, overlap 26; NPC-only 50, ExN-only 82).

Only **2/158** members carry explicit ANK2 localization evidence:

1. **SPTBN1** (β-2-spectrin); NPC+ExN.
   - Explicit ANK2 interaction region **966–1125** (UniProt REGION "Interaction with SPTBN1"; JBC 2025 SBD definition), overlapping Step-3 **ZU5 1 (968–1156)**.
   - **Confidence: high.** Note: not all of 968–1156 is claimed as the binding interface.
   - Relevancy: SPTBN1 carries the ADHD_20 flag in the source workbook (encoded by a gene in the Demontis ADHD exome-seq P<0.001 set); this is a gene-level/network-level note, not a domain-level ADHD statement.
2. **L1CAM**; ExN.
   - Explicit **ANK repeat 11–14** localization (membrane-binding domain site-3; Chen 2017 eLife; Wang 2014). Repeat-level only; **no invented residue interval**.
   - **Confidence: medium.** The residue-level interface is not resolved for L1CAM; the Chirasani R11-pocket validation applies to NrCAM, not L1CAM.
   - L1CAM carries no ADHD flag in the workbook.

**156/158** members are **not_mappable** (no explicit ANK2 binding region in any consulted source).

The correct interpretation: the PPI evidence is **primarily network-level**, with very limited residue/domain-level localization. The 156 not_mappable interactors are **not a domain**; no domain-enrichment statistic is computed from the 2-member mapped subset; the PPI network itself does not localize ADHD function to ZU5 or to the ankyrin repeats.

## 9. Cytoskeletal/synaptic axis

Relevant evidence:

- **ASD variant concentration in the ankyrin-repeat array** (Step 7): 6/11 curated ASD variants, including Ala368Gly at the NrCAM-interacting ANK-11 pocket, which is consistent with disrupting NrCAM binding (exploratory Fisher consistent).
- **ANK2 PPI enrichment for actin cytoskeleton** (GO:0015629, corrected P = 2.77e-39), **cell junctions** (GO:0030054, P = 1.17e-30), **actin binding** (GO:0003779, P = 6.79e-28).
- **Synaptic enrichment:** 70/158 (44.30%) union genes are synaptic (SynGO); synapse GO:0045202 corrected P = 1.52e-29.
- **ASD/DD rare-variant enrichment** in ANK2_Union (KS ASD P = 7.926e-7; DD P = 1e-15).
- **Explicitly localized interactions where appropriate:** L1CAM at ANK repeats 11–14; NrCAM/NF186 are the repeat-array membrane-binding partners of the same motif families (context).

The available evidence is consistent with a cytoskeletal/synaptic axis at the level of (i) the ASD variant distribution (repeat array) and (ii) the interactome composition (actin, junction, synapse). The evidence provides network-level support for this axis but does not establish a domain-level ADHD mechanism within ANK2.

## 10. Excitability/channel axis

Relevant evidence:

- **Cardiac ANK2 variants** (Step 7): 9 curated P/LP variants; sparse localization to ZU5-1/UPA with 5/9 unassigned because of incomplete feature coverage; 7/9 nonsense, frameshift, or splice-site variants with onset positions in ZU5-1 (1091), UPA (1405), and the C-terminal tail.
- **Channelopathy enrichment** among the top-20 ADHD risk genes (corrected P = 2.43e-4), with ANK2 among the overlapping genes (gene-set level).
- **Known cardiac ankyrin-B biology** (ion-channel / excitation-coupling) from the source literature — referenced, not re-established here.

The data do not localize any ANK2 domain to a neuronal excitability function. Channelopathy enrichment is a gene-set-level result and does not establish an ANK2 neuronal excitability mechanism. Cardiac domain localizations should not be extrapolated to ADHD.

## 11. Intersectional evidence

The dataset was examined for evidence connecting ANK2 to both cytoskeletal/synaptic and excitability/channel biology at a shared ANK2 domain or residue.

- No curated observation in this project connects both axes at a single domain or residue.
- The channelopathy handoff is gene-set-level (excitability), while the cytoskeletal/synaptic evidence is network-level and repeat-array-level (ASD variants). Their intersection within ANK2 is not resolved by these data.
- The available data **do not establish an intersectional mechanism**. This is stated plainly; the absence of evidence is noted as a limitation, not as evidence against such a mechanism. No intersectional hypothesis test was performed.

## 12. Hypothesis-by-hypothesis assessment

No numerical scores, rankings, or "winner" labels are assigned. The following uses the allowed conclusion categories (supports / weakly supports / does not distinguish / cannot adequately test).

- **H1a — cytoskeletal convergence** (ADHD via ANK2's cytoskeletal/synaptic mechanism): **The available evidence is consistent with** a cytoskeletal/synaptic axis at the interactome level (actin/junction/synapse enrichments) and at the ASD-variant level (repeat-array concentration). However, the ADHD-specific signal is gene-level, and only 2/158 interactors localize within ANK2. The data **weakly support** H1a at the network level but **do not establish** a domain-level ADHD localization consistent with H1a.
- **H1b — excitability convergence** (ADHD via ANK2's ion-channel/excitation mechanism): Channelopathy gene-set enrichment is consistent at the gene-set level, and ANK2 carries bona fide cardiac-domain variants. But no ANK2 domain is tied to neuronal excitability in this dataset, and channnelopathy overlap does not establish an ANK2 excitation mechanism. The available ADHD evidence provides limited gene-set-level support for an excitability/channel axis, but does not establish that this axis is mediated through ANK2 neuronal function.
- **H1c — intersectional convergence:** The data **cannot adequately test** this hypothesis: no single observation links both axes to a shared ANK2 locus in this dataset.
- **H0 — no preferential localization:** Because there is no ADHD variant-coordinate dataset and ADHD localization evidence is limited to 2/158 interactors, **the data do not distinguish** H0 from the alternative hypotheses for ADHD specifically. For ASD, the exploratory Fisher result is consistent with (but does not prove) preferential repeat-array localization.

The final synthesis may not be forced into any single hypothesis; the dataset is most honestly summarized as: strong gene-level ADHD evidence + network-level mechanistic enrichment + very limited within-ANK2 localization (ASD and cardiac variant sets only, both small).

## 13. What the data support

- ANK2 shows an exome-wide-significant gene-level ADHD rare-variant association in the Demontis dataset (P = 2.273e-6; OR 5.55; pLI = 1.0), with a mixed class I + class II burden architecture.
- The ADHD signal overlaps known ASD/NDD risk biology of ANK2 (ST4 FDR flags; carrier-comorbidity breakdown; interactome overlap with ASD/DD risk genes).
- The ANK2 interactome is enriched for actin-cytoskeletal, cell-junction, and synaptic annotation, and for ASD/DD risk genes.
- The curated ASD variants concentrate in the ankyrin-repeat array with a secondary ZU5-1 cluster (exploratory Fisher consistent but not proof).
- The curated cardiac variants are sparse across ZU5-1/UPA, with most truncations in regions the feature map does not annotate; they are consistent with cardiac ankyrin-B loss-of-function biology from the literature.
- Localization evidence in the 158-member PPI network is limited to two explicit sites: SPTBN1 (966–1125, within ZU5 1; high confidence) and L1CAM (ANK repeats 11–14; medium confidence).

## 14. What the data do NOT establish

- The data do not establish an ADHD domain or residue in ANK2 ("the ADHD domain is…" would exceed the evidence).
- The data do not establish any causal mechanism tying ANK2's ADHD association to cardiac-like channelopathies or to the repeat-array sites.
- The data do not establish that the PPI network localizes ADHD function to ZU5 or to the ankyrin repeats.
- The data do not establish a domain-level intersection of the cytoskeletal/synaptic and excitability/channel axes.
- The exploratory Fisher result does not prove ASD-specific localization and does not describe a mechanism.

## 15. Major limitations

1. No individual ADHD ANK2 protein variant coordinates were available; the ADHD evidence is gene-level.
2. Consequently, no ADHD variant-to-domain mapping was performed, and no ADHD variant-domain distribution was created.
3. The ADHD PPI evidence is primarily network-level (published IP-MS–derived interactome; no per-interactor ANK2 FC/FDR).
4. Only 2/158 ANK2_Union members carried explicit ANK2 localization evidence.
5. The Step-7 ASD/cardiac variant sample is small (11 ASD, 9 cardiac).
6. Several cardiac variants (5/9) are unassigned because of incomplete Step-3 feature coverage; they were not retrospectively assigned.
7. The Step-7 Fisher result is exploratory, sensitive to the small sample, and sensitive to unassigned cardiac variants.
8. The ANK2_Union derives from published IP-MS datasets rather than a new Demontis experiment.
9. Missing structural coverage does not imply absence of structure or disorder; isoform-only AlphaFold models are not canonical Q01484 coverage.
10. Two domain boundaries are lower-confidence than the rest of the Step-3 feature table: Death 1 (1450–1535) is a UniProt-only annotation with no Pfam/InterPro death-domain corroboration, and ANK 24 (793–822) is covered in InterPro only at the ankyrin superfamily/family level, not resolved to the individual-repeat level like ANK 1–23. Both are flagged in `domain_boundaries.csv` (boundary_confidence column) and match the caveat in the README Limitations section; domain coordinates otherwise follow UniProt.

## 16. Final answer to the research question

Within this curated dataset, the functional evidence for ANK2's ADHD association localizes to **gene-level and PPI-network-level architecture only**; it does **not** localize to a specific ANK2 domain or residue, because no curated ADHD variant coordinates exist and because PPI localization is limited to 2 of 158 interactors.

By contrast, the well-characterized comparison mechanisms are expressed at finer granularity in these data:

- **Autism (cytoskeletal/synaptic):** the curated ASD variants localize at the ankyrin-repeat array (6/11; exploratory Fisher consistent) and ZU5 1 (4/11), and the ANK2 interactome is strongly enriched for actin/junction/synapse/NDD-risk biology.
- **Cardiac (ion-channel/excitation):** the curated cardiac variants localize sparsely to ZU5-1/UPA and the C-terminal tail, with a large unassigned fraction; cardiac channelopathy biology is gene-set-level in the ADHD context and should not be extrapolated to ANK2 neuronal function.

The available evidence is therefore **consistent with a cytoskeletal/synaptic axis at the interactome and ASD-variant level** and **weakly, gene-set-level support for an excitability axis**, but the central limitation stands: **localization of the ADHD signal itself is not possible** with the current data. The ADHD association observed for ANK2 is gene-level; its mechanistic localization within ANK2 remains unresolved by the current data.

## 17. Reproducibility / provenance

- All quantitative values are reproduced from the Step 3–9 processed CSVs cited in Section 2; discrepancies (e.g., exact ST4 P = 2.273e-6 vs main-text 2.72e-6) are flagged in `docs/decisions.md`.
- PPI network and enrichments originate from published source tables (Demontis et al. 2025; IP-MS network from published Table S2 of ref 27); flags are defined in the source workbook Overview.
- Domain features originate from UniProt Q01484 (Step 3); structure metadata from PDB/AlphaFold DB (Step 4); variant sets from the cited primary literature and ClinVar (Steps 5–6).
- The only domain-localization inferential test is the pre-specified exploratory Step-7 Fisher test; no additional tests were performed.
- QC before finalizing: all input files verified to exist; Step 7/8/9 counts re-verified against the CSVs; the 158-member union re-verified; SPTBN1 and L1CAM localization re-verified (966–1125 within ZU5 1, high; ANK 11–14 repeat-level, medium); no ADHD coordinates exist; no ADHD domain distribution was created; no new statistical tests were run; no causal claims introduced; `git diff -- PROTOCOL.md` is empty; Step 5–9 datasets verified against live sources in the 2026-09-16 re-execution pass (documented transcription-error corrections logged in `docs/decisions.md`).