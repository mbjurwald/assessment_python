import pandas as pd

#Extract
df = pd.read_csv('imdb_top_1000.csv')

#Transform
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df["Runtime"] = df["Runtime"].str.replace("min", " ")
df["Runtime"] = pd.to_numeric(df["Runtime"], errors="coerce")
df["Gross"] = df["Gross"].str.replace(",", "").astype(float)

#Load 
df.to_csv("imdb_top_1000_clean.csv")


