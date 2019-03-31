import pandas as pd

# Assign spreadsheet filename to `file`
file = 'data\coded_articles.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Blad2')
df2 = df1[['Article', 'Study', 'focal_test']].dropna(subset=['focal_test'])

rng_draw = df2.sample(frac = 1.0).groupby(['Article', 'Study']).head(1)

print(rng_draw)

