# Re-read with appropriate handling in case the user wants proper analysis
df = pd.read_csv(file_path, sep='\t', quotechar='"', engine='python', on_bad_lines='skip')

# Remove any rows with missing Disease Name or Gene ID
df_clean = df.dropna(subset=['Disease Name', 'Gene ID'])

# Group by Disease Name and count unique gene IDs for each disease
disease_gene_counts = df_clean.groupby('Disease Name')['Gene ID'].nunique().sort_values(ascending=False)

# Show top 10 diseases with most unique gene associations
top_10_diseases = disease_gene_counts.head(10)

# Get basic stats
total_unique_diseases = df_clean['Disease Name'].nunique()
total_unique_genes = df_clean['Gene ID'].nunique()
total_rows = len(df_clean)

total_unique_diseases, total_unique_genes, total_rows, top_10_diseases

disease_gene_counts = df.groupby('Disease Name')['Gene ID'].nunique().sort_values(ascending=False)
print("Top diseases by number of associated genes:")
print(disease_gene_counts.head(10))
