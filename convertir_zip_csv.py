import os
import pandas as pd
import zipfile

carpeta_destino = "datos-abiertos"

for c, archivo in enumerate(os.listdir(carpeta_destino)):
    print(archivo)
    if archivo.endswith(".zip"):
        with zipfile.ZipFile(os.path.join(carpeta_destino, archivo), 'r') as zip_ref:
            # Extraer el contenido del archivo ZIP con id
            zip_ref.extractall(carpeta_destino)
            # cambiar el nombre del archivo CSV extraído
            for nombre_archivo in zip_ref.namelist():
                if nombre_archivo.endswith(".csv"):
                    nuevo_nombre = f"datos-{c}.csv"
                    os.rename(os.path.join(carpeta_destino, nombre_archivo), os.path.join(carpeta_destino, nuevo_nombre))
                    # Leer el archivo CSV y convertirlo a Excel
                    df = pd.read_csv(os.path.join(carpeta_destino, nuevo_nombre))
        #os.remove(os.path.join(carpeta_destino, archivo))