import pandas as pd

caminho_arquivo = "exemplo.csv"

df= pd.read_csv(caminho_arquivo)

print(df.head())


df.to_excel("dados_exportados.xlsx", index=False)

print("Arquivo 'dados_exportados.xlsx' salvo com sucesso! 🚀")  