import pandas as pd
import csv

with open(r'C:\Users\user\Downloads\out.csv', "wb") as f:
    csvreader = csv.reader(x.replace('\0', '') for x in f)

df = pd.read_csv(r'C:\Users\user\Downloads\out.csv', sep='\n', encoding='utf-8')

print(df)