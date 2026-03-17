from pathlib import Path
import requests as re

url = "https://ftp.ibge.gov.br/Estimativas_de_Populacao/Estimativas_2025/POP2025_20260113.xls" 

resp = re.get(url, stream=True, timeout=60)
resp.raise_for_status()

outdir = Path(r"C:\Users\jv001\Downloads\GitHub\curso_ebac\data\raw")
outdir.mkdir(parents=True, exist_ok=True)
xls_local = outdir / "Pop_ibge_2025.csv"

with open(xls_local, "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192): 
        if chunk:
            f.write(chunk)
            
print("Arquivo salvo em: ", xls_local)