import pandas as pd

df = pd.read_csv("C:\\Users\\brhva\\Downloads\\archive\\df_file.csv")

reverse_label_mapping = {0: 'Politics', 1: 'Sport', 2: 'Technology', 3: 'Entertainment', 4: 'Business'}

df2 = df.copy()

for label in df2['Label']:
    label = reverse_label_mapping[label]

print(df2.head())