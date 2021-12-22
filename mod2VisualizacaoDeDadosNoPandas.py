import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as ml
import numpy as np

print('\n***************************************\n')

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)

print(df['classification'].value_counts())


plt.figure(figsize=(10, 6))
plt.plot(df['classification'].value_counts(), '|', label='classification',color='#2dcc9c') # configurei a cor para ficar com mesmo tom
plt.bar(df['classification'], height=df['temperatura'], width=0.4, color='#2dcc9c' ) # configuração da barra

plt.show()