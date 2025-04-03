import pandas as pd

# Lendo um DataFrame em formato csv

tabela = pd.read_csv("Data/pandas.csv")

# Imprimindo partes de um DataFrame
'''
print(tabela.head()) # Começo
print(tabela.tail()) # Fim
# O número de linhas a ser imprimido é o parâmetro da função
'''

# Imprimindo um DataFrame
print(tabela) # Primeiras e últimas 5 linhas