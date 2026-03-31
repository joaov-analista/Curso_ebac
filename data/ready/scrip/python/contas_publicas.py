from pathlib import Path
import requests as re

url = "https://ftp.ibge.gov.br/Contas_Nacionais/Financas_Publicas_e_Conta_Intermediaria_de_Governo/2024/Demonstrativo_2024.xlsx" 

resp = re.get(url, stream=True, timeout=60)
resp.raise_for_status()

outdir = Path(r"C:\Users\jv001\Downloads\GitHub\curso_ebac\data\raw")
outdir.mkdir(parents=True, exist_ok=True)
xls_local = outdir / "financas_ibge_2024.csv"

with open(xls_local, "wb") as f:
    for chunk in resp.iter_content(chunk_size=8192): 
        if chunk:
            f.write(chunk)
            
print("Arquivo salvo em: ", xls_local)
