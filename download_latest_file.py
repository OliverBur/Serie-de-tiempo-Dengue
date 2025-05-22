import requests
from bs4 import BeautifulSoup
import time
import zipfile
import os

url = "https://www.gob.mx/salud/documentos/datos-abiertos-bases-historicas-de-enfermedades-transmitidas-por-vector"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
article = soup.find("div", class_="col-article-body")
table = article.find("table")
link = table.find("a")

response = requests.get(link["href"])

filename = time.strftime("%Y%m%d") + "_dengue.zip"

if response.status_code == 200:
    with open(filename, "wb") as f:
        f.write(response.content)
else:
    print(f"No se pudo descargar el archivo. Código de estado: {response.status_code}")

carpeta_destino = "extraido"
os.makedirs(carpeta_destino, exist_ok=True)

with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(carpeta_destino)

os.remove(filename)