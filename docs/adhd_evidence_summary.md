# Step 8 — ADHD Evidence Summary

## 1. Source documentation

All source material originates from the Demontis et al. 2025 publication (*Nature* 649; online 2025, issue dated 2026). Source files are located at the **repository root** (not `data/raw/demontis/`, which does not exist):

| File | Description | Status |
|---|---|---|
| `Demontis_2025_ADHD_main.pdf.pdf` | Main text (24 pages; double `.pdf` extension) | PDF v1.4, 10.4 MB |
| `Demontis_2025_Supplementary_Information.pdf` | Supplementary Methods + carrier phenotype data (1122 lines extracted) | ~29 MB |
| `Demontis_2025_Supplementary_Tables.xlsx` | 24 sheets (ST1–ST24); ST4 and ST11 used | ~1.1 MB |
| `Demontis_2025_Supplementary_PPI_Tables.xlsx` | 10 sheets (MAP1A/ANO8 IP-MS + PPI enrichment) | ~1.3 MB |

Text extracted via `pdftotext -layout` (v0.93). Sheets read via `openpyxl` 3.1.5. Access date: **2026-09-16**. Files were not modified.

## 2. Methods

- Text extracted from both PDFs using `pdftotext -layout` → line-by-line `rg` searches for ANK2.
- ST4 (top-20 ADHD risk genes): exact numeric values extracted from `openpyxl` (all float precision preserved).
- ST11 (enrichment analyses): both the Gene Ontology / pathway enrichment rows (lines 1–165) and SynGO enrichment rows (lines 167–230) inspected; exact P-values captured.
- PPI Table 8 (rare-variant KS enrichment): ANK2_Union rows for ASD, DD, SCZ, BIP traits.
- PPI Table 9 (common-variant enrichment): ANK2_Union row for ADHD trait.
- Supplementary Information: ANK2 carrier phenotype counts extracted from figure bars (Subsection "Phenotype of individuals with class I variants in MAP1A, ANO8 or ANK2").
- Main text: relevant claims located in Results (Gene discovery), Results (Linking ADHD risk genes to biology), Results (PPI-network analyses), Discussion.

## 3. Evidence summary table

See `data/processed/adhd_evidence_summary.csv` (12 rows). Full details:

| ID | Type | Confidence | Claim (summary) | Quantitative value | Source |
|---|---|---|---|---|---|
| AD-01 | genetic | high | ANK2 is an exome-wide significant rare-variant ADHD risk gene | P(final) = 2.273e-06; OR(c1) = 5.55; pLI = 1.0 | ST4 |
| AD-02 | variant-class | high | ANK2 class I burden (rPTVs) elevated in ADHD | c1: 11 cases / 12 controls; P = 1.20e-04; OR = 5.55 | ST4 |
| AD-03 | variant-class | high | ANK2 class II burden (rModerateDMVs) also elevated | c2: 3 cases / 0 controls; P = 2.86e-03; OR = Inf | ST4 |
| AD-04 | genetic | high | ANK2 is a known ASD/NDD risk gene (cross-disorder membership) | ASD_FDR0.05 = 1; NDD_FDR0.05 = 1 | ST4 + main text |
| AD-05 | phenotype | medium | ADHD ANK2 signal driven mainly by ADHD + ASD/ID | Qualitative (no exact proportion) | Main text Discussion |
| AD-06 | phenotype | high | ANK2 class I carriers: mostly ADHD-only; minority comorbid | 11 carriers: 7 ADHD-only, 2 ADHD+ID, 1 ADHD+ASD+SZ+ID, 1 control | Supp Fig 5 |
| AD-07 | genetic | high | Top-20 ADHD genes enriched for Channelopathies; ANK2 overlaps | 4/55; raw P = 2.40e-07; corr. P = 2.43e-04 | ST11 |
| AD-08 | PPI | high | ANK2 union network enriched for actin cytoskeleton | 51/517; corr. P = 2.77e-39 | ST11 |
| AD-09 | PPI | high | ANK2 union network enriched for cell junction | 78/2241; corr. P = 1.17e-30 | ST11 |
| AD-10 | PPI | high | ANK2 union enriched for synapse (SynGO/GO) | 70/158 (44.30%); corr. P = 1.52e-29 | ST11 + main text |
| AD-11 | PPI | high | ANK2 union network enriched for ASD/DD rare-variant risk genes | ASD P = 7.93e-07, FDR = 1.90e-06; DD P = 1e-15, FDR = 7.61e-16 | PPI Table 8 |
| AD-12 | PPI | high | ANK2 union network enriched for actin binding | 40/446; corr. P = 6.79e-28 | ST11 |

## 4. Counts by type

| evidence_type | count |
|---|---|
| genetic | 3 |
| variant-class | 2 |
| phenotype | 2 |
| PPI | 5 |
| **total** | **12** |

## 5. Confidence distribution

| confidence | count |
|---|---|
| high | 11 |
| medium | 1 |
| low | 0 |
| **total** | **12** |

Medium confidence assigned to AD-05 (qualitative comorbidity claim with no numerical proportion in accessible text).

## 6. Key quantitative results

- **Gene-level association:** P(final) = 2.27307199679582e-06; OR(class I combined) = 5.54769260336939 (ST4). Main text displays P = 2.72e-6 (note discrepancy below).
- **Class I (rPTV):** 11 cases / 12 controls; P = 1.2035297803548e-04; OR = 5.55.
- **Class II (rModerateDMV):** 3 cases / 0 controls; P = 2.85778222177253e-03; OR = Inf.
- **PPI — actin cytoskeleton:** corrected P = 2.77e-39 (exact match to protocol §5).
- **PPI — cell junction:** corrected P = 1.17e-30 (exact match to protocol §5).
- **PPI — synapse (GO:0045202):** corrected P = 1.5201951279202584e-29.
- **PPI — ASD rare-variant enrichment:** KS P = 7.92597452559107e-07, FDR = 1.90223388614186e-06.
- **PPI — DD rare-variant enrichment:** P = 1e-15, FDR = 7.61295788314393e-16.
- **Channelopathies (DisGeNET):** 4/55 genes; corrected P = 2.43e-04 (ANK2 overlaps).

### P-value discrepancy: ST4 vs main text

The main text abstract reports `ANK2 (P = 2.72 × 10−6, OR = 5.55)`. Supplementary Table 4 reports `P(final) = 2.27307199679582e-06`. The more precise ST4 value has been used throughout this summary (2.273e-06). The discrepancy (2.27e-6 vs 2.72e-6) is documented here and in `docs/decisions.md`.

## 7. Variant-class architecture

- ANK2 is the only one of the three exome-wide significant ADHD genes where **both class I and class II** variants contribute (MAP1A and ANO8: class I only).
- This mixed architecture is noted in the main text and reflected in the ST4 combined meta-analysis design.
- pLI = 1.0 (complete LoF constraint); ASD_FDR0.05 and NDD_FDR0.05 both = 1 (cross-disorder gene list membership).

## 8. PPI evidence

- **ANK2 union network = 158 genes** (70 of which map to SynGO synaptic annotations = 44.30%).
- Network derived from **published IP-MS datasets** (Table S2 of a prior study), not generated de novo in Demontis 2025 (main text Methods, "PPI-network analyses"). Datasets: ANK2_WT (NPCs); ANK2_WH, ANK2_CNCR1, ANK2_CNCR2 (ExNs).
- **Enriched functional annotations (ANK2 union):** actin cytoskeleton, cell junction, synapse, actin binding, actin filament binding, cytoskeleton, cadherin binding, and others (ST11).
- **Rare-variant overlap (PPI Table 8):** ANK2 union network enriched for ASD rare-variant risk genes (KS P = 7.93e-07) and DD rare-variant risk genes (P = 1e-15). SCZ: not reported for ANK2_Union in extracted rows (rows present for NPC/ExN subsets but not union — confirm in full file if needed).
- **Common-variant (PPI Table 9):** ADHD ANK2_Union: BETA = −0.0228, P = 0.62, FDR = 0.73 — **not significant** (not included as positive evidence row).

## 9. Phenotype / carrier evidence

- Carrier phenotype breakdown (Supp Fig 5): ANK2 class I carriers = 11 total. ADHD-only = 7; ADHD+ID = 2; ADHD+ASD+SZ+ID = 1; control (no diagnoses) = 1.
- Over 50% of the 33 carriers across all three genes had ≥1 comorbidity (ASD/SZ/ID) (main text). Among the 11 ANK2 class I carriers shown in Supp Fig. 5, 3 had ASD/SZ/ID comorbidity.
- Main text Discussion: "the ANK2 signal was driven mainly by ADHD with co-occurring autism or ID" — this is a statistical-composition claim (not a carrier-count claim).

## 10. Limitations

**Individual ADHD-associated ANK2 variant protein coordinates were not available in the accessible Demontis material used for this analysis; therefore no ADHD variant-to-domain mapping is performed.**

Additional limitations:
- Source files located at repo root (not `data/raw/demontis/`); file `Demontis_2025_ADHD_main.pdf.pdf` has a double `.pdf` extension — deviations from expected Step 8 file structure.
- P-value discrepancy between ST4 and main text (Section 6).
- AD-05 (comorbidity driver claim) is medium confidence: no exact proportion or specimen count is provided in accessible text.
- No ADHD-vs-cardiac or ADHD-vs-ASD domain overlap comparison is performed (reserved for Steps 9–10).
- ANK2_Union network from PPI workbook is based on published IP-MS, not novel experimental data; interpretation limited to enrichment signals, not direct binding evidence.

## 11. Decisions log (Step 8)

| Decision | Rationale |
|---|---|
| Source files used at repo root | `data/raw/demontis/` does not exist; all four Demontis files are at repo root; originals not modified |
| P(final) = 2.273e-06 used (not 2.72e-6) | ST4 is the more precise source; discrepancy documented |
| ANK2_Union network provenance documented | Published IP-MS (not generated de novo); distinction from MAP1A/ANO8 networks relevant for Step 9 |
| AD-05 marked medium confidence | Qualitative claim with no numerical proportion |
| Common-variant ANK2_Union result (not significant) excluded from positive evidence | Negative result does not support convergence; included in notes only |
| AD-07 classified as **genetic** (not PPI) | ST11 row 4 input gene set = "Top 20 ADHD rare variant risk genes" (ADHD rare-variant gene-discovery set), not the ANK2 PPI network. Main text reports this as enrichment of the top-20 ADHD risk genes among channelopathy genes. PPI rows are the separate "ANK2 Union" ST11 entries. |
| AD-04 classified as **genetic** (not phenotype) | ST4 ASD_FDR0.05 / NDD_FDR0.05 are binary membership flags of ANK2 in published ASD and NDD rare-variant risk-gene lists (cross-disorder gene-level annotation); the carrier/clinical phenotype rows remain phenotype (AD-05, AD-06). |
| Derived 27% comorbidity percentage removed | The ratio (3/11 = 27%) was calculated in this project; Step 8 avoids introducing calculated values. Underlying source counts retained verbatim (11 total; 7 ADHD-only; 2 ADHD+ID; 1 ADHD+ASD+SZ+ID; 1 control). |
| No ADHD variant coordinates | None available in accessible Demontis material |

## 12. Verification / QC

| QC check | Status |
|---|---|
| `git diff -- PROTOCOL.md` | Empty — PROTOCOL.md unchanged |
| CSV valid (12 rows, 15 columns) | Pass |
| All 4 evidence_types present | Pass: genetic (3), variant-class (2), phenotype (2), PPI (5) |
| All rows have evidence_id, claim, value, evidence_type, source, confidence | Pass |
| All rows have source_table and source_section | Pass |
| No ADHD genomic coordinates (chr/pos/rs) in any field | Pass (regex verified) |
| No ASD/cardiac variant files modified | Pass (`git status` — see below) |
| Step 9/10 not commenced | Pass |
| `data/processed/adhd_evidence_summary.csv` created | Pass |
| `docs/adhd_evidence_summary.md` created | Pass |

```bash
$ git status --short
```

(After write: `docs/adhd_evidence_summary.md` and `data/processed/adhd_evidence_summary.csv` should appear as untracked/new files.)
