# introdução ao pandas


import pandas as pd


def decimal_converter(value): # esta função substitui virgula por ponto
    try:
        return float(value.replace(',', '.'))
    except ValueError:
        return value

# LEITURA DE DADOS

# leitura dos dados csv
df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)

# leitura  de planilhas excel
# 2 abas (worksheets)

# leitura  do arquivo todo
excel_file = pd.ExcelFile('https://pycourse.s3.amazonaws.com/temperature.xlsx')
print(type(excel_file))

print('\n***************************************/\n')

# leitura da primeira sheet1
# dados númericos com separador decimal = '.'
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print(df2)

print('\n***************************************/\n')

# leitura da primeira Sheet2
# dados númericos com separador decimal = ','
# sem o decimal  o dado abriria com uma  virgula inves de um ponto
# # com vigurla o dado vira uma String um objeto e nao conseguimos manipulalo como um float.
df3 = pd.read_excel(excel_file, sheet_name='Sheet2', converters={'temperatura': decimal_converter} ) #chamou a função converters
print(df3)    

print('\n***************************************/\n')

print("**Vizualizando As Primeiras Linhas**\n")
n = 3
print(df.head(n))

print('\n***************************************/\n')

print("**Vizualizando As Ultimas Linhas**\n")
n = 3
print(df.tail(n))

print('\n***************************************/\n')

print("**DTYPES**\n")
print(df.dtypes)

print('\n***************************************/\n')

print("**Estatísticas básicas**\n")
print(df.describe())

print('\n***************************************/\n')

print("**Dataframe Info**\n")
print(df.info())

print('\n***************************************/\n')

print("**Nomes Das Colunas**\n")
print(df.columns)

df.columns = ['coluna 1', 'coluna2', 'coluna3']
print("Mudando o nome das Colunas: ",df.columns)