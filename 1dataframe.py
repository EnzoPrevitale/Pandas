import pandas as pd

# Criando um DataFrame pelo Pandas

df = pd.DataFrame(
    {
        "Nome": ["Enzo", "João", "Paulo"],
        "Idade": [17, 20, 32],
        "Profissão": ["Estudante","Cozinheiro","Policial"]
    }
)

# print(df)


# Imprimindo apenas uma coluna do DataFrame
'''
nomes = df["Nome"]
print(nomes)
'''

# Criando uma série (coluna) pelo Pandas
'''
idades = pd.Series([17, 42, 25], name="Idades")
print(idades)
'''

# Extraindo dados da série
'''
media = df["Idade"].mean()
maximo = df["Idade"].max()
minimo = df["Idade"].min()

print(media)
print(maximo)
print(minimo)

print(df.describe())
'''

