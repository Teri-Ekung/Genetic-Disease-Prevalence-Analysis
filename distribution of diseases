import pandas as pd
import matplotlib.pyplot as plt

# Load the data with proper parsing
file_path = "/Users/teriekung/Downloads/dataset.csv"
df = pd.read_csv(file_path, sep='\t', quotechar='"', engine='python', on_bad_lines='skip')

# Clean NaN rows from disease or gene
df = df.dropna(subset=['Disease Name', 'Gene ID'])

# 1. Unique genes per disease
genes_per_disease = df.groupby('Disease Name')['Gene ID'].nunique().sort_values(ascending=False)

# 2. Diseases per gene
diseases_per_gene = df.groupby('Gene ID')['Disease Name'].nunique().sort_values(ascending=False)

# 3. Top 10 diseases by gene associations
top10_diseases = genes_per_disease.head(10)

# 4. Top 10 genes by disease associations
top10_genes = diseases_per_gene.head(10)

# 5. Plot distribution of gene counts per disease
plt.figure(figsize=(10,6))
genes_per_disease.plot(kind='hist', bins=50, color='red', alpha=0.7)
plt.title('Distribution of Unique Genes Associated per Disease')
plt.xlabel('Number of Unique Genes')
plt.ylabeimport pandas as pd
import matplotlib.pyplot as plt

# Load the data properly
file_path = "/Users/teriekung/Downloads/dataset.csv"
df = pd.read_csv(file_path, sep='\t', quotechar='"', engine='python', on_bad_lines='skip')

# Clean that shit
df = df.dropna(subset=['Disease Name', 'Gene ID'])

# Count how many gene associations each disease has (frequency)
disease_counts = df['Disease Name'].value_counts()

# Plot pie chart
plt.figure(figsize=(12,12))
disease_counts.plot.pie(
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85, 
    shadow=True, 
    wedgeprops=dict(width=0.4)
)
plt.title('Proportion of Gene Associations per Disease')
plt.ylabel('')
plt.tight_layout()
plt.show()
l('Count of Diseases')
plt.show()

# 6. Plot distribution of disease counts per gene
plt.figure(figsize=(10,6))
diseases_per_gene.plot(kind='hist', bins=50, color='blue', alpha=0.7)
plt.title('Distribution of Diseases Associated per Gene')
plt.xlabel('Number of Diseases')
plt.ylabel('Count of Genes')
plt.show()

print("Top 10 Diseases by Number of Associated Genes:\n", top10_diseases)
print("\nTop 10 Genes by Number of Associated Diseases:\n", top10_genes)
