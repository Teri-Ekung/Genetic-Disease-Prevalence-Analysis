import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load that shit right
file_path = "/Users/teriekung/Downloads/dataset.csv"
df = pd.read_csv(file_path, sep='\t', quotechar='"', engine='python', on_bad_lines='skip')

# Clean the crap out (drop rows missing disease or gene)
df = df.dropna(subset=['Disease Name', 'Gene ID'])

# Count gene associations per disease
disease_counts = df['Disease Name'].value_counts()

# Take top 15 diseases for clean-ass graph
top_diseases = disease_counts.head(15)

# Create a list of colors for each bar
colors = plt.cm.get_cmap('tab20', len(top_diseases)).colors

# Plot that colorful motherfucker
plt.figure(figsize=(14,8))
top_diseases.plot(kind='bar', color=colors)
plt.title('Top 15 Diseases by Number of Gene Associations', fontsize=16)
plt.xlabel('Disease Name', fontsize=14)
plt.ylabel('Number of Gene Associations', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
