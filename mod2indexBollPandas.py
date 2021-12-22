'''
indexação booleana

'''
import pandas as pd

print('\n***************************************/\n')

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)
print(df.dtypes)

print('\n***************************************/\n')
# transformando  o tipo da coluna date para datetime

df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)

print('\n***************************************/\n')
# setando index

df = df.set_index('date')
print(df)

print('\n***************************************/\n')
# indexação booleana
# Seleção de exemplos acima de 25 graus

print('\n***Indexação Booleana***\n')
print(df[df['temperatura'] >= 25])

print('\n***************************************/\n')
# Indexação Booleana considerando o datetiem
# Seleção de entradas ate março de 2020.

print('\n***Indexação Booleana Considerando datetime*** \n')
print(df[df.index <= '2020-03-01'])

print('\n***************************************/\n')
# Indexação Booleana considerando o datetiem
# Seleção de entradas ate março de 2020.
# Slice na coluna classification.

print(df.loc[df.index <= '2020-03-01', ['classification']])

print('\n***************************************/\n')
# indexação Booleana Considerando datetime
# Seleção De Entradas Ate Março  de 2020 e 
# Slice de coluna classification

print(df.iloc[df.index <= '2020-03-01',[-1]])