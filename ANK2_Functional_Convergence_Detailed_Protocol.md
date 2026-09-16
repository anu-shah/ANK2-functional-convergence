# ANK2 Functional Convergence Project — Detailed Research Protocol

## Project objective

### Primary research question

**Where does the functional evidence for ANK2's ADHD association localize within ANK2's known domain/mechanism architecture, relative to the well-characterized cardiac (ion-channel/excitation–contraction coupling) and autism (cytoskeletal/synaptic) mechanisms?**

### Hypotheses

**H1a — Cytoskeletal convergence:** ADHD-associated ANK2 biology preferentially converges on cytoskeletal, spectrin-associated, cell-junction and synaptic functions.

**H1b — Excitability convergence:** ADHD-associated ANK2 biology preferentially converges on ion-channel, calcium-handling and membrane-excitability functions.

**H1c — Intersectional:** ADHD-associated ANK2 biology has substantial evidence for both mechanisms, without clear dominance of either.

**H0:** The assembled evidence does not show preferential localization toward either mechanistic axis.

### Critical evidence limitation

The publicly available Demontis et al. material does not provide an accessible individual ADHD-associated ANK2 variant catalogue with protein coordinates. Therefore, this project does **not** claim to map ADHD variants to specific amino-acid positions. ADHD localization is inferred from gene-level association, variant-class information, neuronal PPI/network evidence and phenotype/comorbidity evidence.

---

# PART A — Reproducible research environment

## Step 1 — Create the repository

### Goal
Make the complete analysis reproducible from raw data to processed data, figures and conclusions.

### Tools
- Git
- GitHub
- VS Code
- Python 3.11+
- Jupyter Notebook/JupyterLab

### Suggested repository

```text
ANK2-functional-convergence/
├── README.md
├── PROTOCOL.md
├── LICENSE
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
├── notebooks/
├── src/
├── results/
│   ├── tables/
│   ├── figures/
│   └── statistics/
├── references/
└── docs/
```

### Output
- GitHub repository
- frozen `PROTOCOL.md`
- initial `README.md`
- `requirements.txt` or `environment.yml`

---

# PART B — Establish the ANK2 reference sequence

## Step 2 — Define the reference transcript and protein

### Goal
Create one authoritative coordinate system for every subsequent annotation and variant mapping.

### Tools
- Ensembl
- NCBI RefSeq
- UniProt

### Procedure
1. Identify human ANK2.
2. Determine the MANE Select transcript.
3. Record transcript ID, genomic coordinates, CDS, protein accession and protein length.
4. Compare the transcript/protein mapping with UniProt Q01484.
5. Record isoform information and any coordinate discrepancies.
6. Freeze the selected coordinate system before variant analysis.

### Output
`data/metadata/ank2_reference.yaml`

---

# PART C — Build the ANK2 domain architecture

## Step 3 — Retrieve ANK2 domain and sequence-feature annotations

### Goal
Create the master protein map onto which ASD and cardiac evidence can be projected.

### Tools
- UniProt
- InterPro
- Pfam
- NCBI CDD
- DisProt where applicable

### Record
For every relevant feature:
- feature name
- start residue
- end residue
- source
- evidence type
- access date

Include, where supported:
- ankyrin-repeat/membrane-binding region
- spectrin-binding region
- ZU5 regions
- UPA
- death domain
- C-terminal regulatory region
- intrinsically disordered regions
- known functional sites
- known interaction sites

### Output
`data/processed/domain_boundaries.csv`

### Rule
Do not silently reconcile conflicting domain definitions. If sources disagree, preserve the discrepancy and document which definition is used for each analysis.

---

# PART D — Establish the structural landscape

## Step 4 — Search for experimentally resolved ANK2 structures

### Goal
Determine which regions of ANK2 have experimentally resolved structures and which do not.

### Tools
- RCSB PDB
- PDBe

### Search terms
- ANK2
- ankyrin-B
- ankyrin-2
- Q01484

### Record
For each relevant structure:
- PDB ID
- ANK2 residues covered
- interacting molecule
- experimental method
- resolution where relevant
- biological context
- source/reference

### Output
`data/metadata/ank2_structures.csv`

---

## Step 5 — Retrieve predicted structures

### Goal
Obtain structural models for relevant regions lacking experimental structures.

### Tools
- AlphaFold Protein Structure Database
- Optional: ColabFold for focused predictions

### Required annotation
Every structural region must be labelled as:
- experimental
- predicted/high-confidence
- predicted/low-confidence
- unresolved/disordered

### Output
- structural files in `structures/`
- `data/metadata/structure_coverage.csv`

### Rule
Predicted structure is structural evidence, not experimental validation.

---

# PART E — Build the ASD variant dataset

## Step 6 — Collect ASD-associated ANK2 variants

### Goal
Create a curated and reproducible ASD ANK2 variant reference set.

### Sources
- Kizhner et al. 2025
- SFARI Gene

### Tools
- PDF/browser
- SFARI
- Python/pandas

### Inclusion
Include variants explicitly reported as disease-associated by the selected sources.

### Record
- gene
- HGVS_c
- HGVS_p
- protein_position
- variant_type
- source
- ASD_evidence
- domain
- transcript
- notes

### Output
- `data/raw/asd_variants_raw.csv`
- `data/processed/asd_variants.csv`

---

# PART F — Build the cardiac variant dataset

## Step 7 — Retrieve cardiac ANK2 variants

### Goal
Create a high-confidence cardiac comparator representing established ANK2 cardiac disease.

### Source
ClinVar

### Inclusion criteria
ANK2 variants associated with:
- Long QT syndrome 4
- Ankyrin-B syndrome
- cardiac arrhythmia, ankyrin-B-related

Include:
- Pathogenic
- Likely Pathogenic

Exclude:
- VUS
- unresolved/conflicting classifications under the protocol criteria

### Tools
- ClinVar web interface
- NCBI E-utilities/API
- Python `requests`
- pandas

### Output
`data/processed/cardiac_variants.csv`

---

# PART G — Normalize ASD and cardiac variants

## Step 8 — Standardize coordinates

### Goal
Ensure that ASD and cardiac variants are expressed in the same protein coordinate system.

### Tools
- Ensembl VEP
- NCBI
- UniProt
- Python/Biopython

### Checks
For every variant:
1. Confirm gene = ANK2.
2. Confirm transcript.
3. Confirm HGVS protein notation.
4. Map to Q01484 coordinates.
5. Classify variant type.
6. Flag variants that cannot be confidently mapped.

### Output
- `asd_variants_mapped.csv`
- `cardiac_variants_mapped.csv`
- mapping/error log

---

# PART H — Map variants to domains

## Step 9 — Assign ASD and cardiac variants to protein regions

### Goal
Determine whether ASD and cardiac variants occupy different parts of ANK2.

### Tools
- Python
- pandas
- domain-boundary table

### Procedure
For each residue position:
- identify the domain/feature containing that residue
- retain unmapped positions as explicit `unassigned`
- map truncating variants according to truncation onset

### Output
`results/tables/variant_domain_assignments.csv`

---

# PART I — Quantitative ASD vs cardiac comparison

## Step 10 — Compare domain distributions

### Goal
Provide the strongest quantitative component currently possible with public variant-level data.

### Analyses
Create:
- domain counts
- percentages
- contingency tables

### Statistical tests
Depending on the final dataset:
- Fisher's exact test
- chi-square test
- permutation test

For sparse data, prefer Fisher's exact test or a permutation framework.

### Output
- `domain_distribution.csv`
- `domain_enrichment_statistics.csv`

### Interpretation
This is a quantitative **reference comparison**, not an ADHD-vs-cardiac spatial test, because ADHD variant coordinates are unavailable.

---

# PART J — Structural feature analysis

## Step 11 — Annotate structural environments of ASD and cardiac variants

### Goal
Determine whether phenotype-associated variants differ in structural context, not merely domain location.

### Features
For each structurally mappable missense variant:
- solvent accessibility
- secondary structure
- disorder
- conservation
- structural domain
- interface proximity
- known interaction site
- structural confidence

### Tools
- PDB
- AlphaFold
- DSSP
- Biopython
- FreeSASA
- UniProt
- ConSurf or another conservation resource

### Output
`data/processed/variant_structural_features.csv`

---

# PART K — Establish the cardiac mechanism reference

## Step 12 — Curate established cardiac ANK2 mechanisms

### Goal
Define what “cardiac-like” means before evaluating the ADHD evidence.

### Focus
Collect experimentally supported ANK2 mechanisms involving:
- ion channels
- NCX
- RyR2
- beta-II spectrin
- calcium handling
- excitation–contraction coupling
- membrane localization/excitability

### Output
`data/processed/cardiac_mechanisms.csv`

---

# PART L — Establish the autism mechanism reference

## Step 13 — Curate established ASD ANK2 mechanisms

### Goal
Define the neurodevelopmental/cytoskeletal reference mechanism.

### Record
For each ASD variant/function:
- variant
- domain
- functional consequence
- cellular phenotype
- affected interaction
- cytoskeletal relevance
- synaptic relevance
- experimental evidence
- source

### Output
`data/processed/asd_mechanisms.csv`

---

# PART M — Extract ADHD evidence

## Step 14 — Build a structured ADHD evidence dataset

### Goal
Convert the Demontis study into a machine-readable evidence table rather than relying on narrative interpretation.

### ADHD evidence classes
Record:
1. ANK2 gene-level association
2. effect size
3. variant-class composition
4. neuronal PPI network
5. functional enrichment
6. ASD/DD enrichment
7. comorbidity pattern
8. relevant mechanistic statements

### Output
- `data/processed/adhd_evidence_summary.csv`
- `docs/adhd_evidence_summary.md`

---

# PART N — Obtain and analyze the ANK2 neuronal PPI network

## Step 15 — Extract the ANK2 PPI data

### Goal
Move beyond headline enrichment values and analyze the actual neuronal interaction network.

### Source
Demontis et al. supplementary PPI tables.

### Record
For every ANK2 interactor:
- gene/protein
- experiment
- cell type
- fold change
- FDR
- source dataset

### Output
`data/processed/ank2_adhd_ppi.csv`

---

## Step 16 — Annotate the ADHD PPI network

### Goal
Determine what biological functions are represented by the neuronal ANK2 interaction network.

### Tools
- Gene Ontology
- SynGO
- Reactome
- UniProt
- g:Profiler
- Python/R enrichment tools

### Categories of particular interest
- actin cytoskeleton
- spectrin-associated processes
- cell junction
- synapse
- membrane organization
- ion transport
- calcium handling
- ion channels

### Output
- `ppi_functional_annotations.csv`
- enrichment tables
- network annotation table

---

# PART O — Define the mechanistic axes before final comparison

## Step 17 — Freeze cytoskeletal and excitability reference sets

### Goal
Operationalize H1a/H1b/H1c so the conclusion does not depend on subjective interpretation.

### Axis A — Cytoskeletal/neurodevelopmental
Potential predefined categories:
- actin cytoskeleton
- spectrin-associated biology
- cell junction
- synapse
- neuronal membrane organization
- cytoskeletal organization

### Axis B — Excitability/cardiac
Potential predefined categories:
- ion channel
- calcium handling
- membrane excitability
- excitation–contraction coupling
- NCX
- RyR2
- cardiac conduction

### Rule
Freeze category definitions before the final convergence analysis.

---

# PART P — Quantify functional enrichment

## Step 18 — Test the ADHD ANK2 network against the predefined axes

### Goal
Determine whether the neuronal ANK2 network is enriched for one mechanistic axis more strongly than the other.

### Tools
Python:
- pandas
- scipy
- statsmodels

or R:
- clusterProfiler
- GOSemSim
- fgsea

### Report
For every category:
- observed genes
- background genes
- enrichment ratio
- effect size
- raw P
- FDR-adjusted P

### Output
`results/statistics/adhd_functional_enrichment.csv`

---

# PART Q — Compare ADHD with ASD and cardiac molecular biology

## Step 19 — Calculate network/functional similarity

### Goal
Quantitatively ask whether ADHD-associated ANK2 biology is more similar to ASD or cardiac biology.

### Comparisons
Calculate:
- ADHD ↔ ASD
- ADHD ↔ cardiac
- ASD ↔ cardiac

### Potential metrics
- Jaccard similarity
- overlap coefficient
- cosine similarity
- GO semantic similarity
- shared interaction partners
- shared functional categories

### Tools
- Python
- pandas
- NumPy
- SciPy
- NetworkX

### Output
`results/statistics/mechanistic_similarity.csv`

---

# PART R — Test similarity against a null model

## Step 20 — Perform permutation analysis

### Goal
Determine whether observed ADHD–ASD or ADHD–cardiac similarity is greater than expected by chance.

### Procedure
1. Define the relevant neuronal background.
2. Preserve the ADHD network size.
3. Randomly sample equivalent-size protein sets.
4. Calculate similarity with the ASD reference.
5. Repeat thousands of times.
6. Construct the null distribution.
7. Compare observed similarity with the null.
8. Repeat for the cardiac reference.

### Tools
- NumPy
- SciPy
- pandas

### Output
- `permutation_results.csv`
- null-distribution figures
- empirical P-values/effect sizes

### Important
The null model should preserve relevant background properties where possible, such as expression/availability or network detectability.

---

# PART S — Map ADHD functional evidence onto ANK2 architecture

## Step 21 — Determine candidate ANK2 regions underlying ADHD functions

### Goal
Connect ADHD PPI/function observations to actual ANK2 molecular architecture.

### Procedure
For each ADHD-relevant functional category:
1. Identify relevant ANK2 interactors.
2. Search literature for experimentally characterized ANK2 interaction regions.
3. Map those regions to UniProt/domain coordinates.
4. Determine which defined region is implicated.
5. Grade the evidence.

### Output
`results/tables/adhd_domain_mechanistic_mapping.csv`

### Critical rule
Do not infer “spectrin-binding domain” solely because the PPI network is enriched for actin/cell-junction proteins. Domain assignment must be supported by an interaction/function source.

---

# PART T — 3D structural investigation

## Step 22 — Examine representative ASD and cardiac variants in 3D

### Goal
Move from simple domain localization to molecular structural interpretation.

### Tools
- ChimeraX
- RCSB PDB
- AlphaFold
- Biopython

### For each representative variant
1. Locate the residue.
2. Display local secondary structure.
3. Display neighbouring residues.
4. Determine buried/surface location.
5. Display interaction partner if a structure exists.
6. Examine interface proximity.
7. Compare wild-type and mutant residue properties.

### Output
- structural figures
- structural annotation tables

---

# PART U — Optional computational structural prediction

## Step 23 — Predict effects of selected variants

### Goal
Explore possible effects on stability or local structure for representative variants.

### Tools
- FoldX
- Rosetta
- DynaMut2 or similar free resources

### Candidate analyses
- predicted ΔΔG
- local packing
- electrostatic changes
- interface disruption

### Rule
This is an **optional secondary analysis**. Focus on variants in structurally resolved or high-confidence regions. Predicted structural effects must never be presented as experimentally established pathogenic mechanisms.

---

# PART V — Evidence hierarchy

## Step 24 — Grade the strength of mechanistic evidence

### Goal
Prevent weak inference from being treated as equivalent to direct experimental evidence.

### Evidence levels

**Level 4 — Direct**
- Variant experimentally shown to alter a specific interaction/function.

**Level 3 — Strong indirect**
- Domain or interface experimentally established to mediate a relevant interaction/function.

**Level 2 — Functional association**
- PPI, GO, pathway or network evidence supports the mechanism.

**Level 1 — Contextual**
- Phenotypic comorbidity or general literature association.

### Output
`results/tables/evidence_grading.csv`

---

# PART W — Hypothesis assessment

## Step 25 — Evaluate H1a, H1b, H1c and H0

### Goal
Produce the final inference without confirmation bias.

Create:
`results/hypothesis_assessment.md`

For each hypothesis record:
- evidence supporting
- evidence against
- evidence strength
- evidence level
- major uncertainties
- sensitivity-analysis result
- verdict

Use:
- supported
- partially supported
- not supported
- evidence insufficient

Avoid “proved” or “confirmed” unless the evidence warrants causal language.

---

# PART X — Sensitivity analyses

## Step 26 — Test robustness

### Goal
Determine whether conclusions depend on arbitrary dataset choices.

Repeat key analyses under predefined alternatives.

### Cardiac dataset
- strict ClinVar P/LP
- P/LP plus high-confidence literature variants

### ASD dataset
- SFARI only
- SFARI plus Kizhner dataset

### ADHD PPI
- NPC
- ExN
- Union

### Functional annotations
- GO
- GO + Reactome
- GO + SynGO

### Output
`results/statistics/sensitivity_analysis.csv`

---

# PART Y — Final figures

## Step 27 — Figure 1: ANK2 architecture

### Goal
Orient the reader.

Show:
- major ANK2 domains
- experimental structural coverage
- predicted coverage
- ASD variant locations
- cardiac variant locations

## Step 28 — Figure 2: ASD vs cardiac variant distribution

### Goal
Show the phenotype-specific reference architecture quantitatively.

Use:
- domain distribution
- lollipop plot
- counts/percentages
- statistical results

## Step 29 — Figure 3: ADHD neuronal ANK2 PPI network

### Goal
Show the molecular evidence underlying the ADHD analysis.

Show:
- ANK2
- interactors
- cell type
- functional categories
- optionally interaction frequency

## Step 30 — Figure 4: Mechanistic convergence

### Goal
Show where ADHD evidence falls relative to the two reference mechanisms.

The relative placement must be determined by the analyses rather than assumed.

## Step 31 — Figure 5: Representative 3D structures

### Goal
Demonstrate molecular-level structural reasoning.

Show representative:
- ASD variants
- cardiac variants
- relevant interaction interfaces
- structural context

---

# PART Z — Reproducibility and final write-up

## Step 32 — Automate analysis

### Goal
Allow another researcher to reproduce computational results.

Suggested scripts:

```text
src/
├── download_clinvar.py
├── normalize_variants.py
├── map_domains.py
├── annotate_structure.py
├── ppi_analysis.py
├── enrichment.py
├── network_similarity.py
├── permutation_tests.py
└── generate_figures.py
```

Manual literature curation is acceptable, but every manual decision should be recorded.

---

## Step 33 — Preserve raw and processed data separately

### Goal
Make provenance traceable.

```text
data/
├── raw/
├── processed/
└── metadata/
```

Keep:
- original downloads
- access dates
- source/accession
- scripts
- processed data
- mapping/error logs

Never overwrite raw data.

---

## Step 34 — Write the final report

### Recommended structure

1. Abstract
2. Background
3. Research question
4. Hypotheses
5. Data sources
6. Methods
7. Results
8. Structural analysis
9. Mechanistic synthesis
10. Sensitivity analyses
11. Limitations
12. Conclusion
13. Reproducibility statement

### Central limitation

The project localizes **functional evidence** associated with ADHD to ANK2's molecular architecture; it does not directly localize individual ADHD-associated ANK2 variants because accessible variant-level coordinates are not available.

---

# Minimal software stack

| Task | Recommended tool |
|---|---|
| Literature | PubMed / Google Scholar |
| ASD variants | SFARI + Kizhner et al. |
| Cardiac variants | ClinVar |
| Transcript | Ensembl / NCBI |
| Protein | UniProt |
| Domains | InterPro / Pfam / CDD |
| Structures | PDB / AlphaFold DB |
| 3D visualization | **ChimeraX** |
| Main analysis | **Python** |
| Data handling | pandas |
| Statistics | SciPy / statsmodels |
| Networks | NetworkX |
| Enrichment | g:Profiler / GO / Reactome / SynGO |
| Structure processing | Biopython / DSSP / FreeSASA |
| Optional ΔΔG | FoldX |
| Plotting | Matplotlib |
| Interactive analysis | Jupyter |
| Version control | Git + GitHub |

### Suggested Python environment

```text
pandas
numpy
scipy
statsmodels
matplotlib
networkx
biopython
requests
jupyter
```

---

# Final analytical hierarchy

```text
                 ANK2
                   |
                   ▼
       ADHD genetic association
                   |
                   ▼
        neuronal ANK2 PPI network
                   |
                   ▼
       functional/pathway evidence
                   |
          ┌────────┴────────┐
          ▼                 ▼
   Cytoskeletal axis   Excitability axis
          │                 │
          ▼                 ▼
         ASD             Cardiac
       reference         reference
          └────────┬────────┘
                   ▼
          ANK2 architecture
                   |
                   ▼
          structural analysis
                   |
                   ▼
       mechanistic convergence
                   |
          ┌────────┼────────┐
          ▼        ▼        ▼
         H1a      H1b      H1c
                    or
                    H0
```

**Core principle:** the project should never claim that ADHD variants occupy a particular ANK2 domain. It asks whether the *functional evidence associated with the ADHD ANK2 signal* points toward one of ANK2's established molecular architectures, and then uses ASD/cardiac variant and structural evidence to contextualize that inference.
