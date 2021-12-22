# métopdo groupby
# Operações inplace.
# compartilhamento de memoria em copias.

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as ml
import numpy as np


print('\n***************************************\n')

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')


# OUTRAS OPERAÇÕES UTEIS EM PANDAS.

print(df.head(6))


print('\n***************************************\n')

# grupby: agrupando por valores únicos de uma ou mais colunas
print(df.groupby(by='classification'))

print('\n***************************************\n')

# grupby: agrupando por valores únicos de uma ou mais colunas
print(df.groupby(by='classification').mean())

print('\n***************************************\n')

# groupby: agrupamento por valores unicos de uma ou mais colunas
print(df.groupby(by='classification').sum()) # sum() = soma.

print('\n***************************************\n')

# drop: remoção de colunas.
print(df.drop('temperatura',axis=1))

print('\n***************************************\n')

# cópia de um dataframe: evita compartilhamento de mémória 
# sem copy(), operações inplace em df2 também alteream o df

df2 = df.copy() # Criei um df2 que vai ser a copia do df
print(df2)

print('\n***************************************\n')
print('\n***auterando o df2 com inplace***\n')
df2.drop('temperatura', axis=1, inplace=True)
print(df2.head())