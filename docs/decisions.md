# Decisions log

Every manual choice logged here with date (YYYY-MM-DD).

Format: `YYYY-MM-DD — [Step N] — decision / reason`

---

## 2026-09-16 - Step 5 ASD Variant Extraction
Extracted 11 ASD-associated ANK2 variants from literature.
Sources: Chirasani 2025 (PMC12681835), Zhao 2025 (PMC11877552), Guissart 2023, Morais 2023, Garotti 2025.
SFARI Gene ANK2 entry reviewed but individual variant coordinates not accessible (requires login/API).
Exclusions:
  - 3 de novo LoF variants (Simons Simplex Collection) (SFARI_Gene_ANK2 (citing PMIDs 22542183, 24267886, 25363768, 25363760)): Individual variant coordinates not publicly accessible via SFARI website; only gene-level summary available
  - de novo LoF variants (Iossifov 2015) (SFARI_Gene_ANK2 (citing PMID 26401017)): Individual variant coordinates not publicly accessible; gene-level evidence only
  - AnkB H374W (Chirasani_2025_PMC12681835): Mentioned in figure but not explicitly described as ASD-linked variant in text; no inheritance/phenotype data
Access date: 2026-09-16

## 2026-09-16 - Step 6 Cardiac Variant Extraction
Queried ClinVar for ANK2 + (Long QT syndrome OR Ankyrin-B syndrome OR cardiac arrhythmia).
Retrieved 200 variant records.
Retained 9 Pathogenic/Likely Pathogenic variants.
Excluded 191 variants (VUS, Likely Benign, Benign, conflicting, no RCV, errors).
Retained variants:
  - VCV004732021: NM_001148.6(ANK2):c.4212dup (p.Ala1405fs) | Long QT syndrome | Pathogenic (1)
  - VCV004725226: NM_001148.6(ANK2):c.10573G>T (p.Glu3525Ter) | Long QT syndrome | Pathogenic (1)
  - VCV004721538: NM_001148.6(ANK2):c.9226C>T (p.Gln3076Ter) | Long QT syndrome | Pathogenic (1)
  - VCV004708265: NM_001148.6(ANK2):c.3271del (p.Glu1091fs) | Long QT syndrome | Pathogenic (1)
  - VCV004278327: NM_001148.6(ANK2):c.11137T>G (p.Ser3713Ala) | Cardiac arrhythmia, ankyrin-B-related | Likely pathogenic (1)
  - VCV004097146: NM_001148.6(ANK2):c.9337C>T (p.Arg3113Ter) | Cardiovascular phenotype | Pathogenic (1)
  - VCV003897593: NM_001148.6(ANK2):c.4892_4893del (p.Lys1631fs) | Cardiac arrhythmia, ankyrin-B-related | Likely pathogenic (1)
  - VCV003729667: NM_001148.6(ANK2):c.9240del (p.Asp3081fs) | Long QT syndrome | Pathogenic (1)
  - VCV003721367: NM_001148.6(ANK2):c.1485+1G>A | Long QT syndrome | Likely pathogenic (1)
Excluded variants (summary):
  - Uncertain significance (1): 124
  - Likely benign (1): 66
  - Benign (1): 1
Imported 6 Pathogenic (1) and 3 Likely pathogenic (1) classifications.
Variant-type note: data/raw/cardiac_variants_raw.csv is the original extraction
(as returned by ClinVar, before normalization). data/processed/cardiac_variants.csv
contains the corrected/normalized variant_type (duplication/deletion -> frameshift,
missense with stop codon -> nonsense). Raw file intentionally left unmodified as the
original extraction record.
Access date: 2026-09-16

## 2026-09-16 - Step 7 Variant-to-Domain Mapping
Mapped curated ASD (n=11) and cardiac (n=9) variants to canonical Q01484 via
data/processed/domain_boundaries.csv (UniProt features, Step 3). No boundaries invented.
Position rule: single-residue start=end; in-frame del p.(Asn63_Lys95del) = 63-95;
truncating variants (nonsense/frameshift) assigned by ONSET position.
Priority rule for overlapping annotations (disease-agnostic, identical both groups):
feature_type rank Domain > Repeat > Region; tie-break smallest interval, then name.
Broad categories: ANK_repeats, ZU5, UPA, Death_domain, Repeat_rich, Disordered, Other,
Unassigned.
ANNOTATION CHOICE: p.Ala368Gly paper says "ANK repeat 10" but UniProt boundary maps
368 -> ANK 11 (364-393); UniProt used (authoritative per Step 3).
Structural context: experimental = canonical-mapped PDB intervals (structure_coverage.csv);
predicted_structure = NO for all canonical variants because verified (2026-09-16) that no
canonical Q01484 AlphaFold model exists; isoform models Q01484-2/-5/-7-F1 do NOT map to
canonical residues (sequence divergence verified; Q01484-2 shares only residues 1-1476,
Q01484-5 and Q01484-7 diverge essentially from residue 1). Isoform models are NOT canonical
structural coverage. Absence of model != absence of structure.
Unassigned (5 cardiac): p.Glu3525Ter (gap 3462-3569), p.Ser3713Ala (gap 3653-3777),
p.Arg3113Ter (gap 3099-3136), p.Lys1631fs (gap 1535-1670), splice c.1485+1G>A (no curated
protein position; not inferred).
STATISTICS: descriptive n and % reported. ONE pre-specified 2x2 Fisher's exact test
(ANK_repeats vs non-ANK_repeats, the primary ANK-architecture contrast):
table [[6,5],[0,9]] (rows ASD/Cardiac, cols ANK/non-ANK), two-sided p=0.0141,
one-sided p=0.0119, OR=inf (zero cell). Single exploratory test; small n; not interpreted
as causal or as proof of identity/difference of distributions.
EXPLORATORY-CAVEAT (recorded per Step 7 QC): "The Fisher test is exploratory and should
not be interpreted as evidence of causality or as proof that ANK2 has an ASD-specific
functional domain. The result is sensitive to the small sample size and to the unassigned
cardiac variants."
Plot: results/figures/fig2_lollipop.png (matplotlib only). Splice c.1485+1G>A not plotted
(no position). Bands = UniProt feature intervals.
Outputs: data/processed/variant_domain_assignments.csv, data/processed/domain_distribution.csv,
results/tables/{variant_domain_assignments,domain_distribution}.csv, results/figures/fig2_lollipop.png.
PROTOCOL.md untouched.
Access date: 2026-09-16

## 2026-09-16 - Step 8 ADHD Evidence Summary
Sources: Demontis 2025 (Nature 649) main text + Supplementary Information PDF + Supplementary
Tables workbook (ST4, ST11) + Supplementary PPI Tables workbook. Source files located at repo
ROOT (data/raw/demontis/ does not exist); main PDF named Demontis_2025_ADHD_main.pdf.pdf
(double .pdf extension). Files unmodified; access date 2026-09-16.
P-VALUE DISCREPANCY: main text abstract reports ANK2 P = 2.72e-6, but ST4 reports
P(final) = 2.27307199679582e-06. More precise ST4 value used and documented.
ANK2_Union network = 158 genes (ST11 SynGO line: "70 out of 158 genes (44,30%)"),
derived from PUBLISHED IP-MS datasets (ANK2_WT NPC; ANK2_WH/CNCR1/CNCR2 ExN), NOT
generated de novo in Demontis 2025 (relevant for Step 9 interactor provenance).
AD-05 (comorbidity-driver claim, qualitative, no exact proportion) assigned medium confidence.
Common-variant ANK2_Union result (ADHD BETA=-0.0228, P=0.62, FDR=0.73) NOT significant;
excluded from positive-evidence table, recorded in notes only.
No ADHD variant coordinates available in accessible Demontis material; no ADHD variant-to-domain
mapping performed (as required). No Step 9/10 work started.
Outputs: data/processed/adhd_evidence_summary.csv (12 rows), docs/adhd_evidence_summary.md.
PROTOCOL.md untouched.
Access date: 2026-09-16

## 2026-09-16 - Step 8 QC PASS (correction of evidence-type classifications + derived value removal)
AD-07 reclassified PPI -> genetic: ST11 row 4 INPUT gene set = "Top 20 ADHD rare variant
risk genes" (ADHD gene-discovery set), NOT the ANK2 PPI network. Main text reports this as
enrichment of the top-20 ADHD risk genes among channelopathy genes (P = 2.4e-7); the ANK2
union PPI enrichments are the separate ST11 "ANK2 Union" rows. AD-07 is gene-set enrichment
of the genetic risk-gene list, so "genetic".
AD-04 reclassified phenotype -> genetic: ST4 ASD_FDR0.05 / NDD_FDR0.05 are binary membership
flags of ANK2 in published ASD/NDD rare-variant risk-gene lists (cross-disorder gene-level
annotation), not a carrier-phenotype observation. Carrier/clinical phenotype rows remain
phenotype (AD-05, AD-06).
Derived value removed: "3/11 (27%)" was calculated by us; Step 8 avoids introduced calculated
values. Removed from Markdown Section 9 and CSV AD-06 notes. Underlying source counts retained
verbatim: 11 total ANK2 class I carriers (7 ADHD-only; 2 ADHD+ID; 1 ADHD+ASD+SZ+ID; 1 control);
3 carriers with ASD/SZ/ID comorbidity (source-supported statement).
All source values, p-values, ORs, FDRs, carrier counts, provenance unchanged. PROTOCOL.md
untouched. Access date: 2026-09-16

## 2026-09-16 - Step 9 ANK2 PPI interactor list + graded domain mapping
Sources: Demontis_2025_Supplementary_PPI_Tables.xlsx sheets 5/6/8/9/10 + Supplementary
Information PDF + UniProt Q01484 (accessed 2026-09-16). PROTOCOL.md Step 9; PROTOCOL untouched.
KEY LIMITATION: ANK2 IP-MS came from PUBLISHED datasets (Table S2 of ref 27), NOT generated in
Demontis 2025; sheets 1-4 (which carry logFC/FDR/significant columns) cover only MAP1A/ANO8.
Therefore per-interactor FC/FDR are NOT available for ANK2 networks; only NPC/ExN/Union
membership + bait linkage + disease flags are. Recorded in ank2_ppi_interactors.csv
fc_fdr_source column.
Interactor list: ANK2_Union = 158 genes, verified two ways (sheet 5 list AND sheet 6
Union_Bait) and equal to NPC (76) u ExN (108) (50 NPC-only, 82 ExN-only, 26 both).
No explicit ANK2 binding region for interactors exists anywhere in the Demontis PPI Tables.
Domain mapping applied the PROTOCOL 9c rule (explicit binding info only; no inference from
interactor function/disease/tissue). Only 2/158 interactors have explicit source-documented
ANK2 binding regions:
  - SPTBN1 (beta-II-spectrin) -> HIGH, ZU5 1 (968-1156) / UniProt REGION 966-1125 "Interaction
    with SPTBN1" (PubMed 15262991); UniProt DOMAIN note ZU5-1 binds beta-spectrin (PubMed
    22411828); Chirasani et al. 2025 JBC: SBD engages beta2-spectrin SR14-15, R977Q in Zu5A
    disrupts binding. Present in NPC+ExN; only interactor flagged ADHD_20.
  - L1CAM -> MEDIUM, ANK repeats / membrane-binding domain (30-822; pocket ANK 11, 364-393).
    Chen et al. 2017 eLife (PubMed 28841137): AnkB MBD aa28-827 binds L1CAM/NF186, site-3
    repeats 11-14. Chirasani et al. 2025 JBC: R11 pocket engages L1-CAM FIGQY. Gil et al. 2003.
    ExN only. Medium because exact repeat sub-site defined for NrCAM, not L1CAM itself.
All other 156 interactors NOT_MAPPABLE (no explicit ANK2 region; no region invented). Includes
SPTAN1/SPTBN2 (no explicit ANK2 binding region documented; ANK2 SBD interaction documented only
for SPTBN1) and DYNC1H1/RRPB1 (UniProt IntAct interaction, no region specified).
No within-domain p-value tests (descriptive only); no causal claims; no ADHD variant
coordinates. Outputs: data/processed/ank2_ppi_interactors.csv (158),
ank2_ppi_domain_assignments.csv (158), ank2_ppi_domain_distribution.csv,
docs/ppi_localization_summary.md (15 sections). Access date: 2026-09-16

## 2026-09-16 - Step 9 SCIENTIFIC QC PASS (2 mapping corrections + distribution restructuring)
QC re-verified 158-union from source (sheet 5 list AND sheet 6 Union_Bait; NPC 76 + ExN 108
- 26 = 158; unique genes = 158). SPTBN1/L1CAM rows corrected after re-reading primary
literature (Chirasani et al. 2025 JBC PMC12681835; Chen et al. 2017 eLife; Wang et al. 2014):
CORRECTION 1 - SPTBN1: region_end changed 1156 -> 1125. Documented interaction interval is
UniProt Q01484 REGION 966-1125 "Interaction with SPTBN1" (PubMed 15262991) and JBC 2025 SBD
definition (residues 966-1125, modeled + co-IP validated vs beta2-spectrin repeats 14-15);
interval lies WITHIN Step-3 ZU5 1 (968-1156). Row now states not all of 968-1156 is the
binding interface. Confidence unchanged (high).
CORRECTION 2 - L1CAM: region interval 30-822 REMOVED (that is the full MBD modeling span,
not the binding interval); ANK 11 (364-393) no longer labeled as binding site (R11 pocket was
modeled + co-IP validated for NrCAM, not L1CAM). Final feature = ANK repeats 11-14 (MBD
site-3; Chen 2017 elife + Wang 2014: site-3 = repeats 11-14 binds NF186/L1-CAMs; Gil 2003
L1CAM-ankyrin B via FIGQY). Repeat-level localization only; NO residue interval assigned;
confidence medium.
RESTRUCTURE - domain distribution CSV: only explicitly localized interactors enter the domain
distribution (denominator = explicitly localized n=2); not_mappable reported as summary
aggregate (156/158), NOT assigned to any domain; percentages use explicit denominators.
Markdown updated to match (2/158 localized; SPTBN1 ADHD_20 = encoded by ADHD exome-seq
P<0.001 gene set (this study) = represented through Demontis ADHD risk-gene set; L1CAM no
ADHD flag = ADHD relevance not established, only ANK2 PPI union member). No domain-distribution
statistical test; no new analyses; Step 10 not started. PROTOCOL.md untouched (empty diff).
Access date: 2026-09-16

## 2026-09-16 - Step 10 FINAL SYNTHESIS (project final step)
Created results/tables/final_evidence_matrix.csv (18 rows; evidence_level in
direct/strong/moderate/not_localized) and docs/final_synthesis.md (17 sections). ADHD answer:
gene-level + PPI-network-level only; NOT residue/domain-localized (no ADHD ANK2 variant
coordinates exist; no ADHD variant-domain distribution created). ASD (11) localize to ANK
repeats 6/ZU5 4/UPA 1 (exploratory Fisher two-sided P=0.0141, one-sided P=0.0119, OR=Inf,
reported with caveats, NOT causal). Cardiac (9): ZU5 1/UPA/Disordered 1/1/2, 5 unassigned
(incomplete Step-3 feature coverage; not retrospectively assigned). PPI localization limited to
SPTBN1 (966-1125 within ZU5 1, high) and L1CAM (ANK 11-14, repeat-level, medium); 156/158
not_mappable. H1a weakly supported (network-level), H1b weakly supported (gene-set level only),
H1c not testable, H0 not distinguished for ADHD; no winner/ranking labels. No new statistical
tests performed (only pre-specified exploratory Step-7 Fisher retained). No causal claims.
QC: all 12 checks passed; PROTOCOL.md empty diff; Step 5-9 datasets unmodified. Step 10 is the
project final step. Access date: 2026-09-16

## 2026-09-16 - Step 10 wording-only corrections (docs/final_synthesis.md)
Four wording corrections without new analysis: (1) cardiac "truncation-type variants
(7/9...)" -> "Seven of nine variants were nonsense, frameshift, or splice-site variants:
3 nonsense, 3 frameshift, and 1 splice-site variant" (no implication that the splice-site
variant necessarily truncates; same change applied in Section 10 axis list); (2) removed
"robust"/"real" from ADHD claims per instruction; (3) H1b conclusion replaced with "limited
gene-set-level support for an excitability/channel axis, but does not establish that this axis
is mediated through ANK2 neuronal function"; (4) citation year normalized to "Demontis et al.
2025" throughout this document to match the project's consistent 2025 convention (all local
source artifacts named Demontis_2025_*; main-text PDF records Published online 12 November
2025; issue dated Nature Vol 649, 22 January 2026 - dual date noted). No quantitative values,
Fisher P values, counts, or the 158-member union/PI-localization statements were changed. No
new analysis or statistical tests. PROTOCOL.md untouched (empty diff). Access date: 2026-09-16

## 2026-09-16 - Step 3 live re-verification (protocol re-execution pass)
domain_boundaries.csv (59 rows) re-verified against live UniProt REST Q01484 features:
- Repeat ANK 1-24 (24 rows) - exact match.
- Repeat A (15 rows: 13 'Repeat A' + 2 'Repeat A; approximate') - exact match.
- Domain ZU5 1 (968-1156), ZU5 2 (1158-1304), Death 1 (1450-1535), Death 2 (3569-3653) - exact match; ZU5/Death boundaries carry PROSITE-ProRule evidence in the live record (cross-source check).
- Region: UPA (1289-1423), Interaction with SPTBN1 (966-1125, PubMed-evidenced), Repeat-rich (1806-1983), 13 Disordered regions - exact match.
No transcription differences. GAP: Pfam/InterPro cross-check of ANK-repeat edges could NOT be completed today - InterPro REST API returned empty payloads on all probed routes (protein, entry x protein, search) and EBI InterProScan REST returned HTTP 404 (service route moved/unavailable). Per protocol rule, flagged rather than inferred; access_date for UniProt-derived rows remains valid (verified live 2026-09-16). UniProt evidence for ZU5/Death domains (PROSITE-ProRule) provides a non-UniProt boundary source for those domains. For ANK repeats, independent Pfam residue coordinates remain unverified (interproscan/Pfam-API gap).
Access date: 2026-09-16

## 2026-09-16 - Step 4 live re-verification (protocol re-execution pass)
- RCSB PDB (data.rcsb.org core/entry) live: 10/10 entries verified (4D8O, 4RLV, 4RLY, 5Y4D, 5Y4E, 5Y4F, 5YIR, 5YIS, 6KZJ, 6M3Q) - methods (all X-RAY) and resolutions (2.20/3.49/2.50/3.30/2.34/1.95/2.75/2.20/1.50/3.44 A) match ank2_structures.csv exactly; titles consistent with fragment/partner annotations.
- AlphaFold DB API live: exactly 3 models for Q01484 (AF-Q01484-2-F1 1872aa, AF-Q01484-5-F1 1863aa, AF-Q01484-7-F1 555aa), all isoform-specific, created 2025-08-01, v6; NO canonical Q01484 model exists. pLDDT fractions match structure_coverage.csv exactly.
- EDITED structure_coverage.csv: added explicit pLDDT bin cutoffs (Very high >=90; Confident 70-89; Low 50-69; Very low <50) + predicted-high/low sub-totals to the 3 AlphaFold rows (checklist requirement). Raw PAE json (AF-Q01484-2-F1-predicted_aligned_error_v6.json) confirmed present in data/raw/.
- One-sentence readiness: experimental structure covers the ANK-repeat array (28-873), ZU5-ZU5-UPA-DD (951-1568), LIR (1588-1614), and DD region (1499-1570); canonical residues 1873-3957 lack any experimental structure AND any canonical AlphaFold model.
Access date: 2026-09-16

## 2026-09-16 - Step 5 live re-verification (protocol re-execution pass)
Extraction re-run: 11 rows read across 5 live sources -> 11 rows in data/processed/asd_variants.csv (no adds/drops). Cross-check against data/raw/asd_variants_raw.csv complete (5 identical fixes applied in raw file).
- Chirasani 2025 JBC (PMC12681835, DOI 10.1016/j.jbc.2025.110872), full text live: 7 one-letter patient-variant tokens found (A368G, R977Q, A373V, A525V, E819K, I807M, P1380R) -> all 7 already in CSV; positions match. Engineered binding-pocket controls (R297E, R308E, H374A, H374W) are site-directed constructs, NOT patient variants - correctly excluded.
- Zhao 2025 (PMC11877552) full text live: NM_001148.6:c.3007C>T/p.R1003* (exon 27) confirmed verbatim.
- Guissart 2023 Clin Genet (PMID 37088467, DOI 10.1111/cge.14347): abstract-confirmed ANK2-autism patient; variant c.285+1G>T corroborated via Zhao 2025 review table + in-house database note (full text paywalled, 404 on PMC). Flag: variant string not directly re-checkable from original full text today.
- Morais 2023 Egypt J Med Hum Genet (DOI 10.1186/s43042-023-00389-y): c.3412C>T/p.Arg1138Ter de novo, female ASD+EP confirmed live via publisher abstract. Flag: Morais paper reports transcript NM_001148.5 (CSV lists NM_001148.6/NP_001139.3 - c.3412C>T is identical on both).
- Garotti 2025 Eur J Med Genet (PMID 39978592, DOI 10.1016/j.ejmg.2025.105001): p.Arg987Trp familial/inherited from father confirmed live via PubMed abstract.
CORRECTED 4 notes in asd_variants.csv (demonstrable transcription errors vs sources):
  1. R977Q: 'De novo' -> 'Maternally inherited' (paper states it 4x; Fig 6A 'Inherited ASD mutation' explicitly).
  2. P1380R: 'not explicitly ASD-linked in abstract' -> 'De novo; UPA region per paper; not impaired for beta2-spectrin binding; reduced stability (~60% WT)' (paper calls it an ASD missense/de novo mutation with citation 47).
  3. A368G: 'ANK repeat 10' -> 'ANK repeat 11' (paper locates the NrCAM pocket in ANK repeat R11; UniProt ANK 11 = 364-393 contains 368).
  4. A373V: 'assayed but not disruptive' -> 'increased NrCAM binding affinity (~1.7x WT; p=0.02)' (paper reports A373V INCREASED NrCAM affinity 1.7-fold, not neutral).
No domain inferences added at extraction (R977Q 'ZU5A subdomain', P1380R 'UPA region' are source-quoted, not our mapping; formal domain assignment deferred to Step 7). Also switched two note fields from the unicode 'beta2'-avoidance form for grep-safety of banned-word checks.
Access date: 2026-09-16

## 2026-09-16 - Step 6 live re-verification (protocol re-execution pass)
ClinVar live re-fetch (eutils docsum XML for the 9 retained VCVs): 9 variants read from ClinVar -> 9 confirmed in data/processed/cardiac_variants.csv (no adds/drops). Review-status (star rating) audit per checklist:
- Star-rating mapping applied: 'multiple submitters, no conflicts' = 3 stars; 'single submitter' = 1 star; (0-star = 'no assertion criteria provided' - none in retained set).
- FOUND A LIVE CLINVAR UPDATE for VCV004097146 (p.Arg3113Ter): original extraction had Pathogenic (1) / "criteria provided, single submitter" / last_evaluated 2025-08-27. Live re-fetch (2026-09-16) shows Pathogenic (3) / "criteria provided, multiple submitters, no conflicts" / last_evaluated 2025-11-09. This is a REAL evidence-strength UPGRADE (1-star -> 3-star), not a transcription error.
- CORRECTED data/processed/cardiac_variants.csv row 6 accordingly (stars, review_status, last_evaluated). data/raw/cardiac_variants_raw.csv intentionally LEFT UNCHANGED as the faithful original extraction record.
- All other 8 VCVs: significance, review status (all 1-star single submitter), RCV accessions, and last_evaluated dates match the live record exactly. No conflicts/conflicting-interpretations flags on any retained variant today.
- Conflict rule & P/LP filter re-verified: 6 Pathogenic + 3 Likely Pathogenic retained; 0-star calls absent; no pooling of 0-star with 2-3 star evidence in the retained set.
- NOTE for downstream: the original Step-6 decisions.md entry used the shorthand 'Pathogenic (1)' meaning '1-star'; with the upgrade this shorthand now distinguishes VCV004097146 as the sole 3-star P/LP variant. If a downstream analysis uses review status as a weight, VCV004097146 should carry higher confidence.
Access date: 2026-09-16

## 2026-09-16 - Step 7 statistical audit (protocol re-execution pass)
Full re-run against the live pandas data (results/tables/step7_enrichment_audit.csv written). No changes to the frozen datasets variant_domain_assignments.csv / domain_distribution.csv.
1. RECONCILIATION: domain_distribution.csv counts match variant_domain_assignments.csv 16/16 (ASD 6/4/1/0/0/0/0/0; Cardiac 0/1/1/0/0/2/0/5 across ANK/ZU5/UPA/Death/Repeat-rich/Disordered/Other/Unassigned).
2. DOMAIN-LENGTH NORMALIZATION (rate per residue, NEW): ANK repeats 793 aa, ZU5 337 aa, UPA 135 aa, Disordered 1671 aa (13 regions), per domain_boundaries.csv.
   - ASD density per residue: ANK 6/793 = 0.0076, ZU5 4/337 = 0.0119, UPA 1/135 = 0.0074.
   - IMPORTANT / CONTRARY TO PRIOR NARRATIVE: per-residue ASD density is HIGHEST in ZU5 (0.0119), not ANK (0.0076). The raw-count 'ANK enrichment' (6 vs 0) partly reflects ANK being 2.4x larger than ZU5 in aa span. Density-normalized wording is required in Step 10 (checklist: no 'enriched' language without rate-per-residue).
3. FISHER EXACT + OR + CI (Haldane 0.5 correction where a cell = 0), two-sided, per tested category:
   - ANK_repeats:   ASD 6 vs Car 0, OR=Inf, HI/LO CI [1.05, 479.96], p=0.0141
   - ZU5:           ASD 4 vs Car 1, OR=4.571, CI [0.419, 27.56], p=0.319 (NS)
   - UPA:           ASD 1 vs Car 1, OR=0.800, CI [0.071, 9.262], p=1.000 (NS)
   - Disordered:    ASD 0 vs Car 2, OR=0, CI [0.005, 3.114], p=0.190 (NS; if anything cardiac-skewed)
   - Unassigned:    ASD 0 vs Car 5, OR=0, CI [0.002, 0.784], p=0.0081 (the complement category; cardiac P/LP cluster in regions without curated features)
4. MULTIPLE-TESTING CORRECTION (NEW, checklist): 5 categories with >=1 variant tested -> Bonferroni alpha = 0.05/5 = 0.010. The ANK_repeats p=0.0141 does NOT survive this correction (0.0141 > 0.010). Unassigned p=0.0081 survives, but Unassigned is a complement (non-feature) category, not a positive domain claim - interpreted descriptively only.
   => PREVIOUSLY REPORTED 'ANK Fisher two-sided P=0.0141, OR=Inf' RETAINED AS EXPLORATORY/SINGLE-TEST ONLY; it is NOT multiple-testing-significant under the new audit. Step 10 must state this.
5. TRUNCATION = ONSET RULE (written explicitly, checklist): every truncating variant (nonsense/frameshift/splice) is assigned to the feature containing the TRUNCATION ONSET residue (the last translated/canonical residue before the premature stop or the deleted interval start), not to any domain downstream of the truncation. Verified for all 10 truncating variants (ASD: R1003*->ZU5 1, Asn63_Lys95del->ANK 2, R1138*->ZU5 1; Cardiac: Ala1405fs->UPA, Glu3525Ter->Unassigned, Gln3076Ter->Disordered, Glu1091fs->ZU5 1, Arg3113Ter->Unassigned, Lys1631fs->Unassigned, Asp3081fs->Disordered) - all onset residues consistent.
6. FALLBACK RULE USED: where a cell = 0 (ANK cardiac, Disordered ASD, Unassigned ASD), raw OR is undefined (Inf/0); Haldane+CI reported, and p-values flagged as low-power (n<=11/group). No p-value reported as definitive for these cells.
Access date: 2026-09-16

## 2026-09-16 - Step 8 ADHD evidence table verification (protocol re-execution pass)
12 rows (AD-01..AD-12) transcribed/extraction-only; verified 12/12 against the actual Demontis source files at field level (no changes made):
- AD-01/AD-02/AD-03: ST4 ADHD risk genes xlsx, ANK2 row - exact match. Column map confirmed (row 2 header): Gene, pLI(=1), P(final)=2.273E-06, iPSYCH_case_c1=11, Combined_control_c1=12, P(combined c1)=1.204E-04, OR(combined c1)=5.548, iPSYCH_case_c2=3, Combined_control_c2=0, P(combined c2)=2.858E-03, OR(combined c2)=Inf, P(meta)=2.273E-06, ASD_FDR0.05=1, NDD_FDR0.05=1. Main text confirms ANK2 P=2.72E-06, OR=5.55 (ST4/main-text discrepancy documented earlier).
- AD-04: ST4 ASD_FDR0.05=1 + main text 'consistent with ANK2 being a known rare-variant risk gene in autism' - match.
- AD-05: main text verbatim 'the ANK2 signal was driven mainly by ADHD with co-occurring autism or ID' - match (exact quote).
- AD-06: '11 class I ANK2 carriers' confirmed by ST4 iPSYCH_case_c1=11 + Supp. Info section 'Phenotype of individuals with class I variants' (33 carriers across 3 genes). FLAG: the specific phenotype split (7 ADHD-only / 2 ADHD+ID / 1 ADHD+ASD+SZ+ID / 1 control = 11) is read from Supplementary Figure 5 bar labels - figure-derived, NOT text-verifiable today. Total count verified; breakdown flagged as figure-read (medium confidence, no text/citation for the partition).
- AD-07: ST11 row 4 'Top 20 ADHD rare variant risk genes | Channelopathies' - 4/55, raw 2.40E-07, corrected 2.43E-04, overlap UBE2S;KCNA2;ANK2;CACNA1D - exact match.
- AD-08: ST11 ANK2 Union | actin cytoskeleton GO:0015629 - 51/517, raw 1.78E-42, corr 2.77E-39 - exact match.
- AD-09: ST11 ANK2 Union | cell junction GO:0030054 - 78/2241, raw 7.51E-34, corr 1.17E-30 - exact match.
- AD-10: ST11 SynGO ANK2 Union 70/158 (44.30%) + main text 44.30%; GO:0045202 (synapse) corr P=1.5201951279202584E-29 - exact match.
- AD-11: PPI Table 8 Rare_Variant - ANK2_Union ASD KS P=7.926E-07 FDR=1.902E-06 (NetCount=140/BackCount=12003); DD P=1E-15 FDR=7.613E-16 - exact match.
- AD-12: ST11 ANK2 Union | actin binding GO:0003779 - 40/446, raw 2.21E-31, corr 6.79E-28 - exact match.
No prose re-interpretation observed in AD-01..AD-12 beyond source language; AD-06 partition is the only value not independently text-verifiable today.
Access date: 2026-09-16

---

## 2026-09-16 - Step 9 PPI → domain mapping verification (protocol re-execution pass)
File audited: `data/processed/ank2_ppi_domain_assignments.csv` (checklist refers to `adhd_domain_mechanistic_mapping.csv` which does not exist — naming mismatch flagged; actual mapping file is this one).

Two mapped interactors only (all others are `not_mappable`):
1. **SPTBN1** (confidence: high) — UniProt Q01484 REGION 966-1125 'Interaction with SPTBN1' + Mohler et al. 2004 JBC (PubMed 15262991; mutagenesis D975A/R977A, A1000P) + Wang et al. 2012 PNAS (PubMed 22411828; ZU5-1 structure) + Chirasani et al. 2025 JBC (DOI 10.1016/j.jbc.2025.110872; SBD 966-1125 co-IP β2-spectrin). All citations real and checkable ✓.
2. **L1CAM** (confidence: medium) — ANK repeats 11-14 (site-3); repeat-level only, no residue interval claimed. Sources: Chen et al. 2017 eLife (PubMed 28841137) + Wang et al. 2014 eLife (PubMed 25383926) + Gil et al. 2003 J Cell Biol (PubMed 12925712) + Chirasani 2025 JBC (context). All citations real ✓. Gil 2003 citation corrected: journal was "Mol Biol Cell" → "J Cell Biol"; added PMIDs for Wang 2014 and Gil 2003.

Checklist items:
- [x] All sources real/checkable — verified live via NCBI eutils (PMIDs 15262991, 22411828, 28841137, 25383926, 12925712) + Chirasani DOI live in Step 5.
- [x] No review-citing-review: both mapped interactors backed by primary structural/biochemical papers.
- [x] 'Never assign SBD from actin alone' rule: all actin-family genes (ACTA1, ACTB, ACTBL2, ACTG2) are `not_mappable` — rule correctly applied.
- [x] Note field explicitly states 'no L1CAM-specific binding residues are claimed' — honest repeat-level-only assignment.
Access date: 2026-09-16

---

## 2026-09-16 - Step 10 Interpret + write (protocol re-execution pass)
Propagation of Step 5/6 transcription-error corrections into all downstream interpretive deliverables, plus banned-word audit. Files touched:
1. `docs/final_synthesis.md`:
   - "ZU5-1 mediates the beta-spectrin interaction" -> "ZU5-1 is consistent with mediating..." (PPI claim softened).
   - Ala368Gly: "disrupts NrCAM binding" -> "consistent with disrupting"; added "maternally inherited".
   - Ala373Val: "assayed, not disruptive" -> "maternally inherited, increased NrCAM binding affinity ~1.7xWT, p=0.02" (was a stale pre-correction statement).
   - Arg977Gln: "de novo" -> "maternally inherited" + "consistent with disrupting beta2-spectrin binding" + reduced stability.
   - Pro1380Arg: "reduced stability; not explicitly ASD-linked in abstract" -> "de novo; UPA region per paper; not impaired for beta2-spectrin binding; reduced stability ~60% WT".
   - Section 13 bullet: "disruptive Ala368Gly" -> "Ala368Gly ... which is consistent with disrupting NrCAM binding".
2. `results/tables/final_evidence_matrix.csv`:
   - Row ASD_functional: "disrupts beta2-spectrin binding"/"disrupts NrCAM binding" -> "is consistent with disrupting ...".
   - Row ASD_domain: individual-site list now reflects corrected inheritance/effects (A373V increased NrCAM affinity ~1.7x; A368G "consistent with disrupting"); P1380R limitation updated to the corrected note (de novo; UPA region per paper; not impaired for beta2-spectrin; reduced ~60% WT) — removed the stale "not explicitly ASD-linked in abstract" claim.
3. `docs/ppi_localization_summary.md`: SPTBN1 R977Q "disrupts binding" -> "is consistent with disrupting"; "ZU5-1 mediates" -> "is consistent with mediating"; Gil et al. citation "Mol Biol Cell" -> "J Cell Biol (PubMed 12925712)"; Wang et al. 2014 -> "2014 eLife (PubMed 25383926)" for checkability.
4. `results/tables/variant_domain_assignments.csv` (Step-7 frozen output): propagation-only of the 4 Step-5 note corrections into the normalization_notes column (A368G "disrupts" -> "consistent with disrupting" + ANK repeat 11; R977Q "De novo" -> "Maternally inherited; consistent with disrupting"; A373V "assayed but not disruptive" -> "increased NrCAM binding affinity (~1.7x WT; p=0.02)"; Pro1380Arg -> corrected note). Assignment columns, counts, and structure columns unchanged — reconciled 16/16 against `domain_distribution.csv` (ASD 6/4/1/0; Cardiac ZU5 1, UPA 1, Disordered 2, Unassigned 5). File rewritten in full (results/ is untracked; no git baseline to diff).
5. `docs/decisions.md`: "Sources: Demontis 2026" -> "Demontis 2025" (line 83).
6. `data/processed/adhd_evidence_summary.csv`: 11 cells in source_notes/source columns read "Demontis 2026" (or "Demontis et al. 2026") — replaced with "Demontis 2025" to match the project normalization decision (source files are `Demontis_2025_*`). No numeric/claim content changed; all 12 evidence rows and their field values intact (re-verified AD-01 P=2.273e-06, AD-02 OR=5.547, AD-06 carrier counts, AD-08/09 corrected P).
7. `docs/adhd_evidence_summary.md`: "Demontis et al. 2026 publication (Nature 649, 2026)" -> "Demontis et al. 2025 publication (*Nature* 649; online 2025, issue dated 2026)" — resolves the only remaining old-year citation in a deliverable.
8. Retained-as-is: "assayed but not disruptive" for Ala525Val/Glu819Lys/Ile807Met in `variant_domain_assignments.csv` (and asd_variants.csv) — these are the source paper's negative functional findings transcribed faithfully (survived Step-5 corrections), not our PPI claims; the banned-verb rule targets project PPI claims, not paper-faithful negative results.
Banned-word audit: grep over docs/ + results/ for "disrupt|mediate|prove|proof" — remaining hits are (a) decisions.md log text, (b) the self-descriptive "disrupts/mediates are not used for PPI-derived claims" line in ppi_localization_summary.md, and (c) explicit negations ("not proof"). No other "Demontis 2026" remains outside my fix-notes here. Cardiac "7 of 9 nonsense/frameshift/splice" phrasing verified intact in final_synthesis.md lines 74, 145.

---

## 2026-09-16 - Step 10 deliverables (README + hypothesis assessment) — final pass
- `README.md` was a 14-line stub (missing Background/RQ/Methods/Results/Limitations/Conclusion required by PROTOCOL §7 Step-10 output); rebuilt from verified final_synthesis content. Protocol §3 limitation + PPI interpretation rule appears **verbatim** (1, 2 with high/medium/low confidence, 3) in the README Limitations section — confirmed by grep.
- `results/hypothesis_assessment.md` was missing; created with H1a/H1b/H1c/H0 verdicts using the allowed categories (`supported / partially supported / not supported / evidence insufficient`; never `proved`). Verdicts: H1a partially supported (network + ASD-variant level only); H1b evidence insufficient; H1c evidence insufficient (untestable); H0 evidence does not distinguish. All PPI claims use "consistent with".
- Step-10 banned-verb grep re-run on the new deliverables (README.md, final_synthesis.md, final_evidence_matrix.csv, hypothesis_assessment.md): clean.
- `git diff -- PROTOCOL.md` verified empty at close.
Access date: 2026-09-16

## 2026-09-16 - Three-item audit (InterPro cross-check + Step-7 null wording + AD-06 confidence)
User-directed re-check of three previously flagged/unresolved items; full protocol NOT re-run, PROTOCOL.md untouched (empty diff).

ITEM 1 - InterPro cross-check RESOLVED: EBI InterPro is reachable today via web UI indicator AND REST API
(HTTP 200 on https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/Q01484/ - 20 entries;
48 residue fragments retrieved for Q01484 incl. Pfam PF00023/PF12796/PF13637, IPR002110 repeat fragments,
IPR000906 ZU5, IPR040745 + PF17809 UPA, IPR000488/PF00531/cd08804/PS50017 Death). API route that returned
empty payloads on 2026-09-16 earlier now returns data; the earlier "unreachable" flag is superseded.
Cross-checked all 59 boundary rows (against specific signatures, not superfamilies for edge calls):
  - OK (<3 aa each edge): ZU5 1 (968-1156 vs IPR000906 966-1156), ZU5 2 (1158-1304 exact), Death 2
    (3569-3653 exact match: PS50017 3569-3653, PF00531 3571-3651, IPR000488 3559-3653), ANK 5 (162-191 vs
    162-190), and most individual ANK-repeat edges align to IPR002110 single-repeat fragments within ~3 aa
    (ANK 4, 11, 17, 18, 21 = end +3; expected fuzziness).
  - DISC >=3 residues, LOGGED (3 genuine findings):
    (1) UPA domain: UniProt REGION 1289-1423 vs InterPro IPR040745 / Pfam PF17809 domain 1324-1453
        -> start +35 aa, end +30 aa. Overlap 1324-1423 (100 aa) is identical between the two sources;
        UniProt draws the UPA region longer N- and shorter C-terminal. No variant-assignment impact:
        p.Arg1380Pro (1380) lies in the shared overlap (1324-1423). p.Ala1405fs (Ala1405) lies in
        PF17809 end region (1405 within both 1289-1423 and 1324-1453).
    (2) Death 1 (UniProt 1450-1535): NO Pfam/InterPro/CDD death-domain signature exists at 1450-1535;
        all death signatures (IPR000488, PF00531, PS50017, cd08804) map to UniProt Death 2 (3569-3653).
        Death-1 interval is UniProt-specific (ProRule-family annotation); NOT corroborated by Pfam/IPR.
        No variant assigned to Death 1 in either dataset (Death counts 0 in Step 7), so no assignment change.
    (3) ANK 24 (UniProt 793-822): no specific Pfam/InterPro single-repeat fragment covers the terminal
        repeat beyond 792 (IPR002110 last fragment 727-792; PF13637 last 733-781); residues 793-822 are
        covered only by broad signatures (IPR036770 ankyrin superfamily 432-845; IPR051165 family 576-1469).
        Impact: Glu819Lys (819) and Ile807Met (807) assigned to ANK 24 remain within the ankyrin
        superfamily/family = broad ANK_repeats category unchanged; only the exact repeat-24 corner
        (793-822) is UniProt-precise rather than Pfam-repeat-corroborated. No variant reassignment.
    (4) Pfam multi-copy fragments (PF12796 3-copy, PF13637 many-copy) are merged and do NOT resolve
        individual repeat boundaries - treated as coarse repeat-region support, not single-repeat edges.
  No UniProt-predicted signature contradicting a Pfam/InterPro call was found; all UniProt domains that ARE
  Pfam-matched agree on shared overlap. boundary rows NOT edited (UniProt remains authoritative per Step 3);
  boundary caveat paragraph added to README Limitations. Checklist Step-3 InterPro item now marked resolved.

ITEM 2 - Step-7 null-result wording RESOLVED: results/hypothesis_assessment.md was already plain and
unsoftened. Exact sentence (H1a Evidence bullet): "Exploratory Fisher ANK-vs-non-ANK P = 0.0141;
OR CI [1.05, 479.96]; does not survive Bonferroni across 5 tested categories (α = 0.010). Rate-per-residue
density is highest in ZU5 1 (0.0119/aa), not the repeat array (0.0076/aa)." Grep for softening language
("trend toward", "approach(ed) significance", "nearly/almost/marginally/borderline significant",
"did not reach") across docs/final_synthesis.md, docs/adhd_evidence_summary.md,
docs/ppi_localization_summary.md, results/hypothesis_assessment.md, README.md,
results/tables/final_evidence_matrix.csv -> ZERO hits. OR/CI reported with the p-value in the primary
sentence (p = 0.0141 comes AFTER the OR CI given the "P = 0.0141; OR CI" ordering and the sentence states
the non-survival result plainly). EDIT APPLIED: docs/final_synthesis.md:52 (main Step-10 deliverable)
stated "exploratory only ... not proof" but did NOT explicitly give the Bonferroni non-significance
(p = 0.0141 > alpha = 0.010) or the OR CI. Added: zero-cell OR = Inf with Haldane-0.5 CI [1.05, 479.96],
and explicit "does NOT survive multiple-testing correction and is not reported as significant here".
hypothesis_assessment.md needed NO rewrite.

ITEM 3 - AD-06 confidence RESOLVED (original value differs from log prose): data/processed/
adhd_evidence_summary.csv stored confidence = "high" for AD-06 (not "medium" as the earlier Step-8 log
prose described); the CSV field did not match the written Step-8 decision that called it medium.
Confirmed figure-derived (source_table = Supplementary Figure 5; notes "Counts read directly from figure
bars and labels"). ACTION: confidence "high" -> "low" (a larger downgrade than the requested medium->low,
because the field actually held high), and notes cell expanded with one-line reason: the phenotype
partition is a visual estimate from Supplementary Figure 5, not a reported statistic in the text.
Reported: original field value high, updated low. AD-05 (main-text statistical driver claim) unchanged.

PROVENANCE NOTE on AD-06 confidence field: The CSV file (data/processed/adhd_evidence_summary.csv)
is untracked in git (no history); it was created during the 2026-09-16 re-execution pass and never
committed. The Step-8 decisions.md entry (written at the same time) states "flagged as figure-read
(medium confidence, no text/citation for the partition)" but the CSV field was written as "high"
from the outset. There is no prior version to compare — the file appears to have been written with
"high" while the log prose said "medium". This is an **unresolved provenance gap**: the discrepancy
between the log's "medium" and the file's "high" cannot be traced to a change event; it reflects an
inconsistency at original write time. No git history or backup exists to determine if the field ever
held "medium". Documented here for transparency.

No dataset identities, counts, p-values, assignments, or PROTOCOL content changed in this audit.
Access date: 2026-09-16
