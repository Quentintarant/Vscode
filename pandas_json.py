import pandas as pd

json_data = '{"name": "Balaji", "age": 25, "city": "Chennai"}'

df = pd.read_json(json_data, typ='series')

print(df)
