# Indexação no  pandas 

# metodo iloc()
# metodo loc()

import pandas as pd

print('\n***************************************/\n')

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)

print('\n***************************************/\n')

print("\n***DF HEAD()***\n")
print(df.head())


print('\n***************************************/\n')

print("\n***Seleção De uma Coluna***\n")
print(df['date'])
print(df['temperatura'])

# tipo
print('\n',type(df['date']))
print('\n',type(df['temperatura']))

print('\n***************************************/\n')

# Seleção de multiplas Colunas
print(df[['date', 'classification']])

print('\n***************************************/\n')
print('\n***DF.iloc***\n')

# indexação por indice 
# selecionando todas as linhas e a coluna  1 
# coluna 1: Temperatura

print(df.iloc[:, 1])

print('\n***************************************/\n')
print("\n***DF.loc***\n")
# indexação por nome
# Selecionando todas as linhas e a coluna 1.

print(df.loc[:, 'temperatura'])

print('\n***************************************/\n')
# indexaçao por indice de multiplas colunas

print(df.iloc[:, 1:3])

print('\n***************************************/\n')
# indexação por nome de multiplas colunas
print(df.loc[:, ["temperatura", 'classification']])

print('\n***************************************/\n')
# indexação por nome de multiplas colunas
print(df.loc[:, 'temperatura' :])