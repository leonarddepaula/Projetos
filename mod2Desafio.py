import pandas as pd
import numpy as np

# Lendo do data frame
df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")
print(df.head())

print('\n************************************************************************************\n')

print(df.info())
print('\n************************************************************************************\n')

print(df.dtypes)
print('\n************************************************************************************\n')

df['datetime'] = pd.to_datetime(df['datetime'])
print(df.dtypes)

# quantos registros existem no ano de  2011 (numéro de linhas, numero de colunas)
print('***\nQuantos registros de locação no ano de 2011***\n')

mask = ((df['datetime'] >= '2011-01-01') & (df['datetime'] <= '2011-12-31')) # metodo mask
print(df[mask])
print('\n  linhas e colunas total:',df[mask].shape)

print('\n************************************************************************************\n')

# quantos registros existem no ano de  2012 (numéro de linhas, numero de colunas)
print('***\nQuantos registros de locação no ano de 2012***\n')
mask2 =((df['datetime'] >= '2012-01-01') & (df['datetime'] <= '2012-12-31'))
print(df[mask2])
print('\n linhas e colunas total:',df[mask2].shape)

print('\n************************************************************************************\n')
print('\n***soma dos valores em 2011***\n')
print(df[mask].sum())

print('\n************************************************************************************\n')
print('\n***soma dos valores em 2012***\n')
print(df[mask2].sum())

print('\n************************************************************************************\n')
print(df.columns)

print('\n************************************************************************************\n')
print(df['season'].unique()) #retorna um vetor com 4 posições  que são as estações do ano

# qual estação do ano contém a maior média de locações de bicicletas?
print('\n***Qual estação do ano contém a maoir media de locações de bicicletas***')

print(df['total_count'].groupby(df['season']).mean())

print('\n************************************************************************************\n')

# horario do dia com maior e menor numero de locação
print('\n***Horario do dia com maior e menor fluxo de locação***\n')
print(df['total_count'].groupby(df['hour']).mean().sort_values())

print('\n************************************************************************************\n')

# que dia da semana contém a maior media de locações  de bicicleta?
print('\n***Que dia da Semana Contem a Maior Media de locação de Bicicletas***\n')
print(df['total_count'].groupby(df['weekday']).mean().sort_values())

print('\n************************************************************************************\n')

# as quarta-feiras (weekday = 3), qual o horario do dia contém maior média de locações de bicicleta?
print('\n***Às Quarta-Feira (weekday = 3), qual o hórario do dia contém a maior média de locações de bicicletas***\n')
mask3 = df['weekday'] == 3

print(df[mask3]['total_count'].groupby(df['hour']).mean().sort_values())

print('\n************************************************************************************\n')

# Aos Sabados(weekday = 6), qual o horário do dia contém a maoir média de locações de bicicletas
print('\n***Aos Sabados(weekday = 6), qual o horário do dia contém a maoir média de locações de bicicletas***\n')

mask4 = df['weekday'] == 6

print(df[mask4]['total_count'].groupby(df['hour']).mean().sort_values())