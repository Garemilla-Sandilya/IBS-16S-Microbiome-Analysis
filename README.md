# 16S rRNA Sequencing Analysis of Human Gut Microbiota in IBS Patients

This project investigates the differences in gut microbial communities between healthy individuals and IBS patients using 16S rRNA sequencing and tools such as Mothur, FastQC, Trimmomatic, and statistical visualization.

## Research Question
- What are the characteristic changes in microbial composition in IBS vs controls?

## Sample Info
- 3 Control: SRR5578910.man, SRR5578914.man, SRR5578918.man
- 3 IBS Patients: SRR32883402, SRR32883403, SRR32883421

## Pipeline Overview
1. Download data using SRA Toolkit
2. Quality control (FastQC)
3. Read trimming (Trimmomatic)
4. Sequence processing (Mothur)
5. Taxonomic classification
6. Statistical analysis (Python)
7. Visualization (Volcano plot, PCA, Dendrogram)

##  Scripts
- `scripts/t-test.py`
- `scripts/volcano_plot.py`
- `scripts/meta.sh`

##  Visualization Output
- `volcano_plot.png`
- `pca_plot.png`
- `dendogram_plot.png`

