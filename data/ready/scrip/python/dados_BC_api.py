from pathlib import Path
import requests
import pandas as pd

# REQUISISÃO API BANCO CENTRAL
URL = ("https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase='202501')")

# PARAMETROS DA REQUISICAO
PARAMETROS = {
    "$format": "json", # FORMATO DE RESPOSTA(JSON)
    "$top": 1000000, # NUMERO MAXIMO DE REGISTROS RETORNADOS
}

response = requests.get(URL, params=PARAMETROS, timeout=30)
response.raise_for_status()

# SAIDA DE DADOS BRUTOS
OUTDIR = Path(r"C:\Users\jv001\Downloads\GitHub\curso_ebac\data\raw")
OUTDIR.mkdir(parents=True, exist_ok=True)

OUTFILE = OUTDIR / "pix_municipio_2025.csv"

# CONTEUDO DOS DADOS ESTA EM JASON
dados = response.json()["value"]
# CONVERTER OS DADOS PARA DATAFRAME
df = pd.DataFrame(dados)

# SALVAR O CSV
df.to_csv(OUTFILE, index=False, encoding="utf-8-sig")
print("Arquivo salvo em: ", OUTFILE)