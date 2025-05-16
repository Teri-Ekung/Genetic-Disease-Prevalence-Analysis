import pandas as pd

file_path = "/Users/teriekung/Downloads/dataset.csv"
df = pd.read_csv(file_path, sep='\t', quotechar='"', engine='python')  # engine='python' handles inconsistent rows better

print(df.shape)
print(df.columns)
print(df.head())
df = pd.read_csv(file_path, sep='\t', quotechar='"', engine='python', on_bad_lines='skip')
