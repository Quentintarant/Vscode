import pandas as pd

excel_file_path='FirstCSV.csv'

df=pd.read_csv(excel_file_path)

print(df.tail(1))