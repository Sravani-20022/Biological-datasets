# Biological Dataset Selection: Lung Cancer Gene Expression

## 1. Dataset Overview

This project describes a publicly available genomic dataset related to lung adenocarcinoma (LUAD). The dataset was selected from the National Center for Biotechnology Information (NCBI) Gene Expression Omnibus (GEO).

**Dataset title:** Transcriptomic Profiling of Primary Tumor, Brain Metastasis, and Normal Brain Tissues of Lung Adenocarcinoma (LUAD)

**Dataset accession number:** GSE293159

**Dataset source:** NCBI Gene Expression Omnibus (GEO)

**Dataset URL:** https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293159

## 2. Dataset Description

The dataset contains RNA sequencing (RNA-seq) gene expression data from human lung adenocarcinoma tissues, brain metastases, and normal brain tissues.

It allows researchers to investigate differences in gene expression between primary lung tumors and tumors that have spread to the brain.

The dataset contains 12 samples collected from three tissue groups.

## 3. Dataset Characteristics

| Feature | Description |
|---|---|
| Organism | Homo sapiens (human) |
| Cancer type | Lung adenocarcinoma (LUAD) |
| Data type | RNA-seq |
| Total samples | 12 |
| Primary lung tumor samples | 4 |
| Brain metastasis samples | 4 |
| Normal brain tissue samples | 4 |
| Reference genome | hg19 |
| Supplementary file | GSE293159_rawCounts_hg19.csv.gz |
| File size | 652.6 KB |
| File format | Compressed CSV |

## 4. Research Question

Which genes show different expression levels between primary lung adenocarcinoma tumors, brain metastases, and normal brain tissue?

## 5. Research Objective

The objective is to investigate gene expression differences between the three tissue groups and identify genes that may be associated with lung adenocarcinoma progression and brain metastasis.

## 6. Potential Bioinformatics Analysis

The dataset could be used for the following analyses:

1. Compare gene expression levels between primary lung tumors and brain metastases.
2. Identify differentially expressed genes between the tissue groups.
3. Investigate genes that may be involved in cancer progression and metastasis.
4. Explore potential molecular biomarkers associated with lung adenocarcinoma.

These analyses can be performed using publicly available genomic data and bioinformatics tools without laboratory experiments.

## 7. Related Publication

Yang X, Xu X, Zhang Y, Guo J, et al. PRAME Augments K63-Linked Ubiquitination and Stabilization of METTL3 to Promote Lung Adenocarcinoma Metastasis. *MedComm (2020)*. 2026;7(11):e71066.

**PubMed ID:** 42899254

**Publication URL:** https://pubmed.ncbi.nlm.nih.gov/42899254/

## 8. Conclusion

GSE293159 is a public genomic dataset that provides an opportunity to study gene expression differences between primary lung adenocarcinoma tumors, brain metastases, and normal brain tissue.

The dataset is suitable for a beginner-level bioinformatics project because it has a clearly defined research question, publicly accessible RNA-seq data, and a manageable number of samples.

This project demonstrates how public biological datasets can be selected and described for future computational analysis.

# Data Cleaning and Basic Analysis of Lung Cancer Gene Expression

## 1. Dataset Overview

- Dataset: GSE293159
- Source: NCBI Gene Expression Omnibus (GEO)
- Organism: Homo sapiens
- Data type: RNA-seq raw gene counts
- Samples: 12 (4 primary tumors, 4 brain metastases, 4 normal brain tissues)
- Total gene records: 57,781

## 2. Objective

To perform basic data cleaning, quality checks, and statistical analysis of lung adenocarcinoma gene expression data.

## 3. Methods

Python and pandas were used to load the compressed CSV dataset, inspect its structure, check missing values, identify duplicate gene identifiers, and calculate descriptive statistics.

Matplotlib was used to create a bar graph comparing total raw gene counts across the 12 samples.

## 4. Results

- Dataset contained 57,781 gene records and 12 sample columns.
- No missing values were detected.
- No negative raw counts were detected.
- No completely duplicate rows were detected.
- Two gene identifiers appeared more than once.
- The median raw count was zero across the samples.

## 5. Conclusion

The dataset was successfully loaded and examined using Python. Basic quality checks and descriptive statistics were completed, and a graph was generated to visualize total raw counts across samples.

The analysis provides an initial understanding of the dataset and prepares it for further bioinformatics analysis. Raw counts require appropriate normalization before making biological comparisons between samples.

## 6. Tools Used

Python, pandas, Matplotlib, and NCBI GEO.

## Dataset Source

https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293159
