import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/DELL/Desktop/python/sample.csv')

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Print the DataFrame after removing duplicates
print(df)

df.to_csv('C:/Users/DELL/Desktop/python/sample_no_duplicates.csv', index=False)
