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


# REMOTE BIOINFORMATICS ANALYSIS REPORT

## Title
**Basic Statistical Analysis and Data Visualization of Lung Adenocarcinoma Gene Expression Data Using Python**

## 1. Abstract

Bioinformatics provides computational approaches for analyzing large-scale biological datasets and understanding molecular patterns associated with diseases. In this project, publicly available RNA sequencing (RNA-seq) data associated with lung adenocarcinoma (LUAD) were analyzed using Python. The dataset, GSE293159, was obtained from the National Center for Biotechnology Information (NCBI) Gene Expression Omnibus (GEO).

The dataset contains 57,781 gene records and 12 samples representing three tissue groups: primary lung tumors, brain metastases, and normal brain tissues. Data inspection, missing-value assessment, duplicate identification, negative-count checking, descriptive statistical analysis, and data visualization were performed using Python libraries, including Pandas, NumPy, and Matplotlib.

Two visualizations were generated: a bar chart showing total raw gene counts per sample and a boxplot illustrating the distribution of log-transformed raw gene counts across samples. The analysis provided an initial understanding of the dataset structure, count distribution, and variation between samples. However, the analysis was descriptive and did not establish statistically significant differential gene expression or identify genes responsible for cancer progression.

## 2. Introduction

Lung adenocarcinoma is a major subtype of non-small cell lung cancer. It can spread from the primary tumor to distant organs, including the brain. Understanding gene expression patterns across primary tumors and metastatic tissues can help researchers investigate the molecular changes associated with cancer progression.

RNA sequencing is a widely used technique for measuring gene expression across biological samples. It produces large datasets containing numerical read counts associated with individual genes.

Bioinformatics tools allow researchers to process, inspect, summarize, and visualize these datasets without requiring laboratory experiments for the computational analysis.

In this project, an RNA-seq dataset associated with lung adenocarcinoma was selected to perform basic statistical analysis and data visualization using Python.

## 3. Research Question

How do raw gene count distributions vary across primary lung adenocarcinoma tumors, brain metastases, and normal brain tissue samples?

## 4. Aim

To perform basic data cleaning, statistical analysis, and visualization of publicly available lung adenocarcinoma RNA-seq data using Python.

## 5. Objectives

1. To obtain and inspect a publicly available lung adenocarcinoma gene expression dataset.
2. To load the compressed RNA-seq count matrix using Python.
3. To examine the dataset structure and sample information.
4. To identify missing values, duplicate gene identifiers, duplicate rows, and negative counts.
5. To calculate descriptive statistics for the numerical gene count data.
6. To visualize total raw gene counts across the samples.
7. To examine the distribution of log-transformed gene counts using a boxplot.
8. To interpret the findings and identify the limitations of the analysis.

## 6. Dataset Description

The dataset was obtained from the NCBI Gene Expression Omnibus (GEO).

**Dataset information:**

| Feature | Description |
|---|---|
| Dataset accession | GSE293159 |
| Dataset title | Transcriptomic Profiling of Primary Tumor, Brain Metastasis, and Normal Brain Tissues of Lung Adenocarcinoma |
| Organism | Homo sapiens |
| Cancer type | Lung adenocarcinoma |
| Data type | Bulk RNA sequencing |
| Total gene records | 57,781 |
| Total samples | 12 |
| Primary tumor samples | 4 |
| Brain metastasis samples | 4 |
| Normal brain samples | 4 |
| Reference genome | hg19 |
| File format | Compressed CSV (.csv.gz) |
| Data file | GSE293159_rawCounts_hg19.csv.gz |

**Dataset source:**  
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293159

## 7. Materials and Software

The following computational resources and Python libraries were used:

- Python 3.13
- Python IDLE
- Pandas for data loading, manipulation, and statistical summaries.
- NumPy for numerical operations and logarithmic transformation.
- Matplotlib for graphical visualization.
- Gzip for reading the compressed CSV dataset.

The analysis was performed on a local computer using Python IDLE.

## 8. Materials and Methods

### 8.1 Dataset Download

The RNA-seq raw count matrix was downloaded from the NCBI GEO database. The downloaded file was named GSE293159_rawCounts_hg19.csv.gz.

### 8.2 Dataset Loading

The gzip library was used to open the compressed CSV file in text-reading mode. Pandas was used to read the contents into a DataFrame.

The dataset was initially inspected using the head() function to display the first five records.

### 8.3 Dataset Structure Assessment

The shape attribute was used to determine the number of rows and columns.

The dataset contained 57,781 rows and 13 columns. The first column contained gene identifiers, while the remaining 12 columns represented the RNA-seq samples.

### 8.4 Data Quality Assessment

The following quality checks were performed:

**Missing values:** The isnull() function was used to identify missing values across the dataset.

**Duplicate gene identifiers:** Duplicate gene identifiers were identified using the duplicated() function on the first column.

**Negative values:** Numerical columns were checked for negative raw counts.

**Duplicate rows:** The duplicated() function was used to identify completely identical rows.

The gene identifier column was also processed using the strip() function to remove leading and trailing whitespace.

### 8.5 Descriptive Statistical Analysis

Pandas describe() was used to calculate descriptive statistics for the numerical sample columns.

The following statistical measures were obtained:

- Count
- Mean
- Standard deviation
- Minimum
- First quartile (25%)
- Median (50%)
- Third quartile (75%)
- Maximum

These statistics were used to understand the distribution and variation of raw gene counts across samples.

### 8.6 Visualization 1: Total Raw Gene Counts per Sample

The numerical sample columns were selected, and the sum of gene counts was calculated for each sample.

A bar chart was generated using Matplotlib to compare the total raw counts across all 12 samples.

The graph was saved as sample_gene_counts.png.

### 8.7 Visualization 2: Gene Count Distribution Across Samples

The NumPy log1p() function was applied to the numerical gene count data.

This transformation calculates log(1 + count), allowing large and small count values to be displayed on a more manageable scale.

A boxplot was generated to visualize the distribution of transformed gene counts across the 12 samples.

The graph was saved as gene_count_distribution.png.

## 9. Results

### 9.1 Dataset Structure

The dataset contained 57,781 gene records and 13 columns, including one gene identifier column and 12 sample columns.

The three sample groups were represented as follows:

- Primary tumor: primary1, primary2, primary3, primary4.
- Brain metastasis: BrM1, BrM2, BrM3, BrM4.
- Normal brain: normal1, normal2, normal3, normal4.

### 9.2 Data Quality Results

The quality assessment produced the following results:

| Quality parameter | Result |
|---|---:|
| Total gene records | 57,781 |
| Total sample columns | 12 |
| Missing values | 0 |
| Duplicate gene identifiers | 2 |
| Negative raw counts | 0 |
| Completely duplicate rows | 0 |

Two gene identifier values, 1-Mar and 2-Mar, appeared more than once. These identifiers require verification against the original gene annotation before any correction or removal. No rows were deleted on the basis of these duplicate identifiers.

### 9.3 Descriptive Statistical Results

Descriptive statistics were calculated for all 12 numerical sample columns.

The median raw count was zero across the samples, indicating that at least half of the gene records in each sample had zero raw counts.

The mean and standard deviation varied between samples, indicating differences in their raw count distributions.

Some genes showed very high raw counts compared with the majority of genes, resulting in a wide range of values.

### 9.4 Visualization 1: Total Gene Counts per Sample

**Figure 1. Total Raw Gene Counts per Sample**

[Insert sample_gene_counts.png here]

The bar chart displayed the total raw gene counts for all 12 samples.

Primary1 showed the highest total raw count, approximately 23.9 million, while normal4 showed the lowest, approximately 14.7 million.

The primary tumor samples showed relatively higher total counts than several brain metastasis and normal brain samples. Variation was also observed within the brain metastasis and normal brain groups.

**What the chart shows:**

- Differences in total raw gene counts between samples.
- Variation in the overall count totals.
- Potential differences in sequencing library sizes.

**What the chart does not prove:**

- It does not establish that primary tumors have higher biological gene expression.
- It does not identify differentially expressed genes.
- It does not demonstrate that any gene causes cancer progression or brain metastasis.

Total raw counts can be influenced by sequencing depth and other technical factors.

### 9.5 Visualization 2: Gene Count Distribution Across Samples

**Figure 2. Gene Count Distribution Across Samples**

[Insert gene_count_distribution.png here]

The boxplot displayed the distribution of log-transformed raw gene counts across all 12 samples.

Most gene records showed low or zero counts, while a smaller number of genes displayed considerably higher counts. Several high-count observations appeared as outliers.

The distributions differed across samples, indicating variation in the spread of raw gene counts.

**What the chart shows:**

- The distribution of gene counts within each sample.
- The median and interquartile range.
- The presence of unusually high count observations.
- Differences in the spread of counts between samples.

**What the chart does not prove:**

- It does not establish statistically significant differences between tissue groups.
- It does not identify specific cancer-associated genes.
- It does not establish a causal relationship between gene expression and metastasis.

The visualization is descriptive and should not be interpreted as a differential expression analysis.

## 10. Discussion

The analysis demonstrated that the GSE293159 dataset could be successfully loaded and examined using Python.

The dataset contained 57,781 gene records and 12 samples representing primary lung tumors, brain metastases, and normal brain tissues.

No missing values or negative raw counts were detected. However, two gene identifiers appeared more than once and require verification using the original annotation.

The descriptive statistics showed that the raw count distributions were highly variable, with median values of zero across samples. The visualizations further demonstrated differences in total counts and count distributions between samples.

The total-count bar chart indicated differences in overall raw counts, while the boxplot showed the presence of many low-count observations and a smaller number of high-count observations.

These observations provide an initial understanding of the dataset's structure and quality. However, differences in raw counts may reflect technical factors, including sequencing depth, rather than biological differences alone.

Further analysis using appropriate normalization and statistical differential expression methods would be required to investigate genes associated with lung adenocarcinoma progression and brain metastasis.

## 11. Limitations

1. The dataset contained only 12 samples, with four samples in each tissue group.
2. The analysis was limited to basic data cleaning, descriptive statistics, and visualization.
3. Raw gene counts were not normalized for sequencing depth or other technical factors.
4. No formal statistical differential gene expression analysis was performed.
5. The two duplicate gene identifiers were identified but not resolved because their original annotation requires verification.
6. The boxplot and bar chart provide descriptive information but do not establish biological significance.
7. The normal brain samples and primary lung tumor samples represent different tissue types, which should be considered when interpreting comparisons.
8. No gene-level functional enrichment, pathway analysis, or biomarker validation was performed.

## 12. Future Scope

The analysis can be extended using established bioinformatics methods.

Future work may include:

- Verification of gene identifiers using the original GEO annotation.
- Quality assessment and normalization of raw RNA-seq counts.
- Differential gene expression analysis using DESeq2 or edgeR.
- Identification of genes associated with brain metastasis.
- Functional enrichment analysis using Gene Ontology and KEGG pathways.
- Investigation of candidate genes and molecular pathways involved in lung adenocarcinoma progression.

These additional analyses may provide further insight into the molecular characteristics of primary tumors and brain metastases.

## 13. Conclusion

The project successfully demonstrated basic bioinformatics data handling and statistical analysis using a publicly available lung adenocarcinoma RNA-seq dataset.

The compressed gene expression dataset was loaded using Python, and data quality checks were performed to assess missing values, duplicate identifiers, duplicate rows, and negative counts.

Descriptive statistics were calculated, and two visualizations were generated to examine total raw gene counts and their distribution across 12 samples.

The results provided an initial overview of gene count variation and dataset quality. However, the findings are descriptive and cannot establish statistically significant gene expression differences or identify molecular mechanisms responsible for metastasis.

Overall, this project provided practical experience in computational analysis, data cleaning, statistical summarization, and visualization of biological data using Python.

## 14. References

1. National Center for Biotechnology Information. Gene Expression Omnibus (GEO). GSE293159: Transcriptomic Profiling of Primary Tumor, Brain Metastasis, and Normal Brain Tissues of Lung Adenocarcinoma (LUAD). Available at: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE293159

2. National Center for Biotechnology Information. RNA-seq counts generated by NCBI GEO. Available at: https://www.ncbi.nlm.nih.gov/geo/info/rnaseqcounts.html

3. Yang X, Xu X, Zhang Y, Guo J, et al. PRAME Augments K63-Linked Ubiquitination and Stabilization of METTL3 to Promote Lung Adenocarcinoma Metastasis. MedComm (2020). 2026;7(11):e71066. doi:10.1002/mco2.71066. PMID: 42899254. Available at: https://pubmed.ncbi.nlm.nih.gov/42899254/

4. The pandas development team. pandas: Python Data Analysis Library. Available at: https://pandas.pydata.org/

5. Harris CR, Millman KJ, van der Walt SJ, et al. Array programming with NumPy. Nature. 2020;585:357–362. doi:10.1038/s41586-020-2649-2.

6. Hunter JD. Matplotlib: A 2D Graphics Environment. Computing in Science & Engineering. 2007;9(3):90–95. doi:10.1109/MCSE.2007.55.
