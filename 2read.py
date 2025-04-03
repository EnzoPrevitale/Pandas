import pandas as pd
import openpyxl

# Lendo um DataFrame em formato csv
tabela = pd.read_csv("Data/pandas.csv")

# Imprimindo partes de um DataFrame
"""
print(tabela.head()) # Começo
print(tabela.tail()) # Fim
# O número de linhas a ser imprimido é o parâmetro da função
"""

# Convertendo para excel
tabela.to_excel("tabela.xlsx", sheet_name="tabela", index=False)

# Imprimindo um DataFrame
# print(tabela) # Primeiras e últimas 5 linhas

# Imprimindo tipos dos dados
#print(tabela.dtypes)

# Informações técnicas de um DataFrame
# print(tabela.info())


