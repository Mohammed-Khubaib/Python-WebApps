import pandas as pd

df = pd.read_csv('sorted_sorted_file.csv')

print(df['College'].to_csv)
df['College'].to_csv('output.csv')