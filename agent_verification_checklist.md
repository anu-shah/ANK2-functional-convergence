# Agent Verification Checklist — ANK2 Protocol

Use alongside PROTOCOL.md. Give these constraints to the agent explicitly per step, not just as background context — models tend to drift from stated discipline (e.g. "do not infer yet") unless it's repeated at the point of execution.

## General rules for every step
- [x] Confirm the agent used a **live fetch/browse**, not memory, for any web source (Ensembl, UniProt, RCSB, AlphaFold, ClinVar, SFARI, g:Profiler). If it can't confirm live access, treat the access_date field as invalid. — PASS 2026-09-16: UniProt REST, Ensembl REST, RCSB (graphql), AlphaFold DB API, ClinVar eutils esummary/docsum, NCBI eutils pubmed esummary, PMC XML/EUtils — all live; InterPro/InterProScan live access unavailable (flagged, not inferred).
- [x] Have the agent report **row counts in vs. out** at each extraction step (e.g. "47 rows read from PDF → 47 written to CSV"). Silent drops are the main failure mode for table transcription. — Steps 5/6: 11 in → 11 out; 9 in → 9 out; 16/16 Step-7 reconciliation; AD rows 12/12.
- [x] Ask the agent to show intermediate output (the actual dataframe/table), not just a prose summary of what it did.

## Step 3 — Domain boundaries
- [x] Spot-check 2–3 domain boundary calls (especially ANK repeat edges) against Pfam or InterPro, not UniProt alone. — RESOLVED 2026-09-16: InterPro REST live (HTTP 200; 20 entries, 48 Q01484 fragments incl. PF00023/PF12796/PF13637 ANK repeats, IPR000906 ZU5, IPR040745/PF17809 UPA, IPR000488/PF00531/PS50017 Death). All 59 rows cross-checked; ZU5 1/2 + Death 2 exact; 3 genuine ≥3-aa findings logged: UPA 1289-1423 vs 1324-1453, Death 1 (1450-1535) uncorroborated by Pfam/IPR, ANK 24 (793-822) terminal repeat only superfamily-covered. No variant reassignment needed (overlaps shared; P1380R/1405fs in UPA overlap; no Death-1 variants; E819K/I807M still ANK superfamily). boundaries.csv not edited (UniProt authoritative).

## Step 4 — Structure coverage
- [x] Confirm explicit pLDDT (and ideally PAE) cutoffs are stated in structure_coverage.csv for the predicted-high/predicted-low split — not just applied silently. — pLDDT cutoffs: VH≥90, C 70–89, L 50–69, VL<50; PAE present in raw json.

## Step 5 — ASD variants
- [x] Enforce "do not infer domains yet" as a literal instruction at extraction time. — PASS: extraction-only; domain assignment deferred to Step 7.
- [x] Re-extract a random ~10% of rows independently (fresh prompt, no memory of prior extraction) and diff against the original as a self-check. — PASS: independent regex re-extraction matched 7/7 Chirasani positions; 4 transcription errors found in original and corrected in processed + raw files (logged).

## Step 6 — Cardiac variants
- [x] Confirm the conflict rule and P/LP filter also account for ClinVar **review status (star rating)** — 0-star calls are much weaker evidence than 2–3 star and shouldn't be pooled without a flag. — PASS: 6 P + 3 LP retained; star-rating mapping documented; VCV004097146 upgraded 1★→3★ on re-fetch (corrected); no 0★, no conflicts.

## Step 7 — Map + tally
- [x] Verify the contingency table and Fisher's exact/odds ratio by reading the actual pandas output, not a stated p-value. — PASS: pandas/scipy output verified (scipy 1.18.1, pandas 3.0.5); audit file `step7_enrichment_audit.csv`.
- [x] Confirm domain-length normalization (rate per residue, not raw count) is present before any "enriched" language is used. — PASS: ANK 0.0076/aa, ZU5 0.0119/aa, UPA 0.0074/aa; ZU5 highest per-residue, reported.
- [x] Confirm multiple-testing correction (Bonferroni/FDR) if Fisher's exact is run across more than one domain. — PASS: 5 categories tested, α=0.010; ANK p=0.0141 does NOT survive; ZU5 p=0.319 n.s.; stated plainly.
- [x] Confirm odds ratios with CIs are reported alongside p-values. — PASS: ANK OR=Inf CI[1.05,479.96]; ZU5 OR=4.571 CI[0.419,27.56]; UPA OR=0.8 CI[0.071,9.262]; Disordered OR=0 CI[0.005,3.114]; Unassigned OR=0 CI[0.002,0.784].
- [x] Get the "truncation = onset" position-assignment rule written out explicitly, not left implicit. — PASS: verified for all 10 truncating variants.

## Step 8 — ADHD evidence table
- [x] Enforce "no prose re-interpretation" literally — each row should be a claim/value/source transcription, not a paraphrase-with-added-inference. — PASS: 12/12 rows field-verified against Demontis source files; AD-06 phenotype split flagged as figure-derived (not text-verifiable).

## Step 9 — PPI → domain mapping (highest hallucination risk)
- [x] Every source in `adhd_domain_mechanistic_mapping.csv` must be a **real, checkable link or DOI** — spot-check a sample yourself against the actual paper. — NOTE: checklist-file name mismatch — file is `ank2_ppi_domain_assignments.csv`. PASS 2026-09-16: SPTBN1 (UniProt 966–1125; Mohler 2004 PMID 15262991; Wang 2012 PMID 22411828; Chirasani DOI 10.1016/j.jbc.2025.110872) and L1CAM (Chen 2017 PMID 28841137; Wang 2014 PMID 25383926; Gil 2003 PMID 12925712) all live-verified; Gil journal corrected Mol Biol Cell→J Cell Biol.
- [x] Confirm no domain assignment rests on a review citing another review; require direct biochemical/structural evidence for a binding-site claim. — PASS: both mapped interactors backed by primary structural/biochemical papers.
- [x] Confirm the "never assign SBD from 'actin' alone" rule was actually applied — check a few borderline rows. — PASS: all actin-family genes (ACTA1, ACTB, ACTBL2, ACTG2) are not_mappable.

## Step 10 — Interpret + write
- [x] Confirm banned verbs ("disrupts," "mediates," "proves") don't appear for PPI-based claims — grep the output file for them directly rather than trusting a self-report. — PASS 2026-09-16: grepped docs/ + results/; PPI "disrupts"→"consistent with disrupting" in final_synthesis.md, final_evidence_matrix.csv, ppi_localization_summary.md, variant_domain_assignments.csv; "mediates"→"consistent with mediating". Remaining hits are log text / self-descriptive / explicit negations. Paper-faithful negative findings ("assayed but not disruptive") retained.
- [x] Confirm the limitation §3 language appears verbatim in the README Limitations section, as the protocol requires. — PASS: README.md built (was stub) with §3 verbatim; `results/hypothesis_assessment.md` created (was missing).