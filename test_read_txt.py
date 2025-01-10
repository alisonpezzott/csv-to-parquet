import os
import pandas as pd

df = pd.read_csv('txt/TotalApontamentoPeriodo1512202415012025.txt', sep=';', encoding='Latin1')
print(df.head())

