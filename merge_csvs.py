import os

import pandas as pd

carpeta_destino = "datos-abiertos"

df = pd.DataFrame()

for archivo in os.listdir(carpeta_destino):
    if archivo.endswith(".csv"):
        data = pd.read_csv(os.path.join(carpeta_destino, archivo), encoding="latin1")
        # append the data to the dataframe
        df = pd.concat([df, data], ignore_index=True)
df = df.drop_duplicates()
df = df.dropna()
df.to_csv("dengue.csv", index=False)