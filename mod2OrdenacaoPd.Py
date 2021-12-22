#ordenação em pandas

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



print('\n***************************************\n')

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)

print('\n***************************************\n')
# df.sort_values
# help(df.sort_values)

print('\n***Ordenação crescente por uma coluna(temperatura)***\n')
# Ordenação crescente por uma coluna

print(df.sort_values(by='temperatura'))

print('\n***Ordenação crescente por uma coluna(classification)***\n')
# Ordenação crescente por uma coluna 

print(df.sort_values(by='classification'))

print('\n***************************************\n')

print('\n***Ordenação Crescente  por mais de uma coluna***\n')
# Ordenação Crescente  por mais de uma coluna

print(df.sort_values(by=['classification', 'temperatura']))

print('\n***************************************\n')

print("\n***Ordenação decrescente por uma coluna***\n")
# Ordenação decrescente por uma coluna

print(df.sort_values(by='temperatura', ascending=False))

print('\n***************************************\n')
# ordenação crescente pelo indice

print('\n***Ordenar Crescente Pelo Indice***\n')
print(df.sort_index())

print('\n***************************************\n')
# ordenação de forma decrescente pelo indice

print('\n***Ordenar Descresente pelo indice\n')
print(df.sort_index(ascending=False))

df['date'] = pd.to_datetime(df['date']) # transformou o data

print(df.dtypes)

# setando index

df = df.set_index('date')
print(df)


plt.figure(figsize=(10, 5))
plt.plot(df['temperatura'], '-o',linewidth=2.5, color='purple', label='temperatura') 
# linhdas No style poderia ser '--' ou '-.'
# configurando a cor da linha
plt.legend()
plt.xlabel('date')
plt.ylabel('')
plt.grid()
plt.show()



plt.figure(figsize=(10, 6))
plt.plot(df['classification'].value_counts().sum(),'|', label='classification',color='#2dcc9c') # configurei a cor para ficar com mesmo tom
plt.bar(df['classification'],height=df['temperatura'], width=0.4, color='#2dcc9c' ) # configuração da barra

plt.show()



# pie plot
plt.figure(figsize=(10, 7))
plt.plot(df['classification'].value_counts())
plt.pie(df['temperatura'], labels=df['classification'], autopct='%1.1f%%')
plt.legend()
plt.xlabel('')
plt.ylabel('')
plt.grid()
plt.show()