# ANK2 PPI Interactor List + Graded Domain Mapping (Step 9)

Access date: 2026-09-16. Protocol: PROTOCOL.md v2.0, Step 9.

## 1. Purpose and scope

This step builds the ANK2 protein-protein interaction (PPI) interactor list reported in the Demontis et al. 2025 ADHD paper and grades how confidently each interactor can be placed on an ANK2 protein region. It does **not** assign domains by inference; an interactor is mapped to a region **only** where a source explicitly specifies ANK2 binding information. The output grounds Step 10 in genes rather than p-values alone.

## 2. Source files and access date

- `Demontis_2025_Supplementary_PPI_Tables.xlsx` — sheets 5 (PPI_Networks), 6 (Interactor_Annotations), 8 (Rare_Variant), 9 (Common_Variant), 10 (Rare_Variant_constraint). Access date 2026-09-16.
- `Demontis_2025_Supplementary_Information.pdf` — checked for ANK2 binding-region statements (none present beyond provenance).
- UniProt Q01484 (ankyrin-2, isoform 4) features/INTERACTION annotations; UniProt KB flat file, accessed 2026-09-16.
- Literature with explicit ANK2 binding-region evidence: Wang et al. 2012 PNAS (PubMed 22411828); Chen et al. 2017 eLife (PubMed 28841137); Chirasani et al. 2025 JBC (doi 10.1016/j.jbc.2025.110872); Gil et al. 2003 Mol Biol Cell; UniProt-cited Mohler et al. 2004 JBC (PubMed 15262991).
- Domain features: `data/processed/domain_boundaries.csv` (Step 3, frozen UniProt Q01484 feature map).

## 3. Provenance of the ANK2 PPI networks

The Demontis 2025 study **did not generate de novo** ANK2 IP-MS. The ANK2 PPI networks were derived from **published IP-MS datasets included in Table S2 of a previous study (reference 27 of Demontis 2025)**. Index proteins for ANK2: ANK2_WT in hiPSC-derived neural progenitors (NPC) and ANK2_WH / ANK2_CNCR1 / ANK2_CNCR2 in excitatory neurons (ExN). The Demontis PPI Tables that contain raw IP-MS peptide/FC/FDR columns (sheets 1-4) cover only MAP1A and ANO8, **not** ANK2. Consequently, per-interactor log2 FC and FDR values are not available for ANK2 networks from this workbook; network membership (NPC/ExN/Union) is available from sheet 5. This limitation is recorded in `ank2_ppi_interactors.csv` (`fc_fdr_source` column) and in `docs/decisions.md`.

## 4. Interactor list construction

- Two independent extractions agree: sheet 5 (PPI_Networks) network lists and sheet 6 (Interactor_Annotations) `Union_Bait` column both give **158 ANK2 interactors** for `ANK2_Union`.
- NPC network membership = 76; ExN membership = 108; NPC-only = 50; ExN-only = 82; present in both = 26.
- `ANK2_Union` (158) == `ANK2_NPC ∪ ANK2_ExN`, verified programmatically.
- Output: `data/processed/ank2_ppi_interactors.csv` (158 rows; columns `gene, cell_type, union_bait, union_nBait, npc_bait, npc_nBait, exn_bait, exn_nBait, ADHD_20, ADHD_GWAS, ASD_72, ASD_185, DD_309, DD_477, NDD_373, NDD_664, SCZ_10, SCZ_32, fc_fdr_source`).

## 5. Network composition by cell type

| Cell type | n interactors | Notes |
|---|---|---|
| ANK2_NPC | 76 | hiPSC-derived neural progenitors (published IP-MS, Table S2 of ref 27) |
| ANK2_ExN | 108 | hiPSC-derived excitatory neurons (published IP-MS) |
| Both NPC and ExN | 26 | shared interactors |
| ANK2_Union | 158 | NPC ∪ ExN |

## 6. Interaction evidence available per interactor

Per interactor, the Demontis PPI Tables provide:
- Linked index protein(s) per cell type (`npc_bait`, `exn_bait`; e.g., ANK2, or ANK2+MAP1A/ANO8 for shared interactors) and counts (`*_nBait`).
- Disease-gene membership flags (see Section 7).
- No ANK2 residue/domain/construct information, and no FC/FDR for ANK2 (Section 3).

Twenty-two interactors are also linked to other baits (Union_nBait 2-3, e.g. ANK2+MAP1A/ANO8); e.g., NPM1, YWHAE, ATP5F1C, CACNA2D1, CAPZA1, CEP170, EPB41L3, HNRNPA1, HP1BP3, HSPA1A, HSPA5, HSPA8, IGF2BP1, MAP1B, MAP6, NCL, NONO, PGAM5, RPL10A, RPL18, RPL18A, RPL27, RPL34, RPL6, RPL7, RPLP2, SOGA3, SYNCRIP, VIRMA, YWHAQ, YWHAZ. Their ANK2 network membership stands on the ANK2 IP-MS analysis; shared-bait linkage does not change membership in the ANK2 network.

## 7. Disease-gene overlap within the ANK2 interactor set

From sheet 6 flags (protein encoded by a gene in the listed curated/GWAS gene sets):

| Flag | n interactors | Flag | n interactors |
|---|---|---|---|
| ADHD_20 | 1 (SPTBN1) | DD_309 | 14 |
| ADHD_GWAS | 0 | DD_477 | 18 |
| ASD_72 | 2 | NDD_373 | 16 |
| ASD_185 | 7 | NDD_664 | 26 |
| SCZ_10 | 0 | SCZ_32 | 0 |

SPTBN1 (βII-spectrin) is the sole interactor in the ADHD gene set and is one of the two interactors mappable to an explicit ANK2 region (Section 12).

## 8. Rare-variant enrichment of ANK2 networks (PPI Table 8)

Kolmogorov–Smirnov enrichment of rare-variant burden in ANK2 networks vs background (network genes expressed in iPSC-derived neurons):

| Trait | ANK2_NPC P (FDR) | ANK2_ExN P (FDR) | ANK2_Union P (FDR) |
|---|---|---|---|
| ASD | 1.52e-05 (3.17e-05) | 3.49e-05 (6.70e-05) | 7.93e-07 (1.90e-06) |
| DD | 1.60e-08 (4.27e-08) | 1.65e-13 (4.95e-13) | 1e-15 (7.61e-16) |
| SCZ | 0.93 (n.s.) | 0.11 (n.s.) | 0.19 (n.s.) |
| pLI (less) | 1.05e-06 (2.39e-06) | 1e-15 (3.20e-15) | 1e-15 (0) |

## 9. Common-variant enrichment of ANK2 networks (PPI Table 9)

MAGMA-style regression of GWAS generative-signal scores on network membership. For ANK2_Union: ADHD P = 0.62 (not significant); ASD P = 0.30; SCZ P = 0.054; BIP P = 0.030; MDD P = 0.69; height P = 0.53. No network is significantly enriched for ADHD common variants; no within-domain p-value tests are performed (Step 9 guardrail).

## 10. Rare-variant constraint analysis of ANK2 networks (PPI Table 10)

KS enrichment split by pLI constraint of the network genes:

| Trait | Network | All P (FDR) | pLI >= 0.9 P (FDR) | pLI < 0.9 P (FDR) |
|---|---|---|---|---|
| ASD | Union | 1.41e-06 (8.00e-06) | 0.13 (0.28) | 1.57e-03 (4.70e-03) |
| DD | Union | 1e-15 (6.85e-15) | 0.61 (0.73) | 8.62e-07 (5.17e-06) |

Constraint-truncating variants carry the Ank2 network signal: the enrichment is driven by pLI < 0.9 genes (loss-of-function constrained set retained), while pLI >= 0.9 subsets are not significant.

## 11. Domain-mapping method and confidence levels

Mapping rule (PROTOCOL.md Step 9c + Step 9 operation instruction): an interactor is assigned to an ANK2 region **only** when a source explicitly provides ANK2 binding information (UniProt feature/domain annotation, UniProt-cited interaction, or literature stating an ANK2 construct/region). No region is inferred from the interactor's function, cell type, disease association, sequence similarity, or structure.

Confidence levels:
- **high** — source directly specifies an ANK2 residue interval or domain for the interaction.
- **medium** — source specifies an explicit ANK2 construct/region (indirect mapping to the feature).
- **low** — relevant evidence but ambiguous.
- **not_mappable** — no defensible ANK2 localization.

Domain features from the frozen Step 3 map (`domain_boundaries.csv`). No within-domain statistical tests; descriptive counts only. No causal claims.

## 12. Domain-mapping results

Among the 158 ANK2_Union members, explicit ANK2 localization evidence was identified for **2 interactors**. The other 156 members have no explicit ANK2 binding region in the source material and are recorded as **not_mappable**; no region was inferred from protein function, cellular localization, disease association, or network membership.

**SPTBN1 (βII-spectrin, UniProt Q01082) — `high`, interaction region 966-1125 within ZU5 1.**
- Explicit ANK2 interaction interval: **residues 966-1125**, from UniProt Q01484 REGION "Interaction with SPTBN1" (PubMed 15262991; mutagenesis D975A/R977A and A1000P prevent SPTBN1 binding) and from Chirasani et al. 2025 JBC, which define the AnkB spectrin-binding domain as residues 966-1125 and model/co-IP-validate its engagement of β2-spectrin repeats 14-15 (R977Q in Zu5A is consistent with disrupting binding).
- This interval overlaps the Step-3 ZU5 1 domain (968-1156). **Primary feature: ZU5 1.** The full ZU5 1 domain extends to residue 1156; the wording here does not claim that all of 968-1156 is the binding interface — the documented interaction interval is 966-1125.
- UniProt DOMAIN note (PubMed 22411828): ZU5-1 is consistent with mediating the interaction with β-spectrin.
- Cell-type presence: NPC + ExN (both).
- ADHD relevance: **represented through the Demontis ADHD risk-gene set** — SPTBN1 is encoded by a gene in the ADHD exome-seq P < 0.001 set (sheet 6 `ADHD_20 = True`), the only ANK2 interactor with this flag. (It is also flagged in the DD/NDD gene sets.) It is not part of the ANK2 PPI evidence alone.

**L1CAM — `medium`, ANK repeats 11-14 (membrane-binding domain site-3).**
- Experimentally supported binding region: **ANK repeats 11-14** (MBD site-3), at repeat level.
  - Chen et al. 2017 eLife (PubMed 28841137) and Wang et al. 2014 eLife (PubMed 25383926): AnkB membrane-binding-domain binding studies define site-3 = repeats 11-14 as a binding site for the L1-CAM family (NF186/L1CAM).
  - Gil et al. 2003 J Cell Biol (PubMed 12925712): L1CAM–ankyrin B binding via the conserved FIGQY motif (Y1229).
- **Primary feature: ANK 11-14** (Step-3 repeats: ANK 11 364-393, ANK 12 397-426, ANK 13 430-459, ANK 14 463-492), listed for orientation only.
- **No residue-level binding interval is assigned.** A narrower "ANK repeat R11 pocket" (H374; ASD sites A368/A373) was modeled and co-IP validated by Chirasani et al. 2025 JBC for **NrCAM** (which shares the conserved FIGQY motif), not for L1CAM itself; it is used here only as supporting context and is not labeled as the L1CAM binding site. The repeat-level localization (11-14) is the experimentally supported claim; "30-822" is the full MBD model span, not the L1CAM binding interval.
- Cell-type presence: ExN only.
- ADHD relevance: **not established as ADHD-specific** — L1CAM does not carry any Demontis ADHD/ASD/DD/NDD/SCZ flag (sheet 6 all `False`); its relevance is only as a member of the ANK2 PPI union.

All other 156 interactors: **not_mappable** — no explicit ANK2 binding region in the Demontis PPI Tables, UniProt Q01484 features/INTERACTION, or the consulted literature. This includes:
- SPTAN1 (αII-spectrin), SPTBN2 (βIII-spectrin) — spectrin family members whose ANK2 *network* membership is documented but for which no explicit ANK2 binding region is documented (the ANK2 SBD interaction is documented only for βII-spectrin/SPTBN1).
- DYNC1H1, RRBP1 — interact with ANK2 per UniProt INTERACTION/IntAct, but no ANK2 region is specified.

## 13. Domain distribution and confidence summary

Among the 158 ANK2_Union members, explicit ANK2 localization evidence was identified for 2 interactors:

| Domain distribution of explicitly localized interactors | confidence | n | denominator | % of that denominator |
|---|---|---|---|---|
| Interaction with SPTBN1 (966-1125), feature ZU5 1 (968-1156) | high | 1 (SPTBN1, NPC+ExN) | explicitly localized interactors | 50.0 |
| ANK repeats 11-14 (MBD site-3), feature ANK 11-14 | medium | 1 (L1CAM, ExN) | explicitly localized interactors | 50.0 |

| Summary | n | denominator | % of that denominator |
|---|---|---|---|
| Explicitly localized interactors | 2 | ANK2_Union members (N=158) | 1.3 |
| No explicit ANK2 localization (not_mappable; not assigned to any domain) | 156 | ANK2_Union members (N=158) | 98.7 |

This distribution reflects only the 2 interactors with explicit localization evidence of the 158 union members; it is **not** representative of all 158 interactors, and it is **not** a statistical comparison of PPI domain distributions (no p-value or enrichment test was performed). The remaining 156 members are not_mappable because the source material supplies an interactor list without ANK2 binding coordinates; assigning additional domains would require unverifiable inference and is refused by the Step 9 rule.

## 14. Guardrails: explicitly not claimed

- No interactor is mapped to an ANK2 region from its function, tissue, disease, or sequence similarity alone ("actin" does not imply a spectrin-binding-domain assignment).
- No ANK2 binding coordinates are invented; ref 27's Table S2 was not accessible, so no construct-level bait mapping is asserted for individual interactors.
- No p-values compare domain distributions; no Fisher tests; no causal statements ("disrupts/mediates" are not used for PPI-derived claims).
- No ADHD variant coordinates are created (consistent with the project's stated boundary).
- not_mappable interactors are recorded as not_mappable — they are not converted into guessed domains.

## 15. Output files, reproducibility, and QC

Files produced:
- `data/processed/ank2_ppi_interactors.csv` (158 rows) — interactors with cell-type membership, bait linkage, disease flags, FC/FDR provenance note.
- `data/processed/ank2_ppi_domain_assignments.csv` (158 rows) — per-interactor region, confidence, source, note.
- `data/processed/ank2_ppi_domain_distribution.csv` — region-level count table.

QC summary:
- ANK2_Union count (158) verified two ways: sheet 5 network list and sheet 6 Union_Bait; equal to NPC ∪ ExN (76, 108, 26 shared).
- Confidence distribution sums to 158; percentages sum to 100.0.
- All mapped regions trace to a citable source specifying ANK2 coordinates/constructs; all other rows are `not_mappable` with a source/note explaining the absence of explicit evidence.
- `git diff -- PROTOCOL.md` empty after this step; Steps 9/10 of the quantitative variant work remain untouched.
- Domain features used from frozen `data/processed/domain_boundaries.csv` (Step 3); variant files (Steps 5-7) and evidence summary (Step 8) not modified.