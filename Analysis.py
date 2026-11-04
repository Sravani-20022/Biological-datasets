import numpy as np

log_counts = np.log1p(counts)

plt.figure(figsize=(10, 6))
log_counts.boxplot()

plt.title("Gene Count Distribution Across Samples")
plt.xlabel("Samples")
plt.ylabel("Log-transformed Raw Counts")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("gene_count_distribution.png", dpi=300)
plt.show()

