import requests
import pandas as pd


# ENDPOINT (exemplo público do BCB)

url = ("https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/""versao/v1/odata/TransacoesPixPorMunicipio(DataBase='202501')")

params = {
    "$format": "json",
    "$top": 10000
}


# REQUISIÇÃO

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()


# CONVERTE PARA DATAFRAME

data = response.json()
df = pd.DataFrame(data.get("value", []))


# EXIBE AS PRIMEIRAS LINHAS
print(df.head())

# SALVA COMO CSV

df.to_csv("bcb_tabela.csv", index=False, encoding="utf-8-sig")

print("Arquivo salvo como bcb_tabela.csv")


df.columns = [col.lower() for col in df.columns]

print("Colunas renomeadas:")
print(df.columns.tolist())

for col in df.columns:
    if "valor" in col or "quantidade" in col:
        df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nTipos de dados após ajuste:")
print(df.dtypes)    

print("\nValores nulos antes:")
print(df.isnull().sum())

df = df.dropna()

print("\nShape após remover nulos:", df.shape)

duplicados = df.duplicated().sum()
print("\nDuplicados antes:", duplicados)

df = df.drop_duplicates()

print("Duplicados após tratamento:", df.duplicated().sum())

print("\nTipos finais:")
print(df.dtypes)
print("\nValores nulos finais:")
print(df.isnull().sum())
print("\nDuplicados finais:", df.duplicated().sum())   
print(df.head())

df.to_csv("dados_tratados.csv", index=False, encoding="utf-8-sig")
df.to_csv("dados_tratados.parquet", index=False, encoding="utf-8-sig")