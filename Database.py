import pandas as pd
import sqlite3

# Open Connection to SQLite database
con = sqlite3.connect("../publications.sqlite")

# Read CSV into a pandas DataFrame
df = pd.read_csv('../scholars_publications.csv', sep="\t")
print(df.head())
df.to_sql('table_name', con, if_exists='replace', index=False)

# verify that result of SQL query stores the dataframe
df2 = pd.read_sql_query("SELECT * from table_name", con)
print(df2.head())

con.close()
