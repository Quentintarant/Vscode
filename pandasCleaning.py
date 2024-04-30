
import pandas as pd

df = pd.read_csv('C:/Users/DELL/Desktop/python/sample.csv')

# df['Date'] = pd.to_datetime(df['Date'])
# df.loc[4, 'Number of employees'] = 45

df.drop_duplicates(inplace = True)
print(df.duplicated())
# print(df.to_string())