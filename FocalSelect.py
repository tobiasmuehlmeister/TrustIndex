import pandas as pd

# Assign spreadsheet filename to `file`
file = 'data\coded_articles.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Loads the sheet from the excel file ("Blad2"  in this case)
df1 = xl.parse('Blad2')

# filters the loaded sheet for the columns Article, Study, and focal_test, deletes missing values in focal_test
df2 = df1[['Article', 'Study', 'focal_test']].dropna(subset=['focal_test'])

# "groupby" creates hierarchical groups. First for the "Article" column, then for the "Study" column
# First it groups all rows from article 10, then it groups all rows from study 1, 2 or 3
# after that, the code draws a sample of 1 from each grouped study
rng_draw = df2.sample(frac = 1.0).groupby(['Article', 'Study']).head(1)

# this prints the draw in total (with article and study number)
print(rng_draw)

# this prints just the focal_test
print(rng_draw[['focal_test']])