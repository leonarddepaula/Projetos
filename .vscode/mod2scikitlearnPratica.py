from os import startfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# classificação de padroes no scikit-learn 

df = pd.read_csv('https://pycourse.s3.amazonaws.com/temperature.csv')
print(df)

print('\n***************************************\n')

x, y = df[['temperatura']].values, df[['classification']].values
print('x: \n', x)

print('\n***************************************\n')

print('y: \n', y)

# pré- processamento
from sklearn.preprocessing import LabelEncoder

# converção de y  para valores numericos
le = LabelEncoder()
y = le.fit_transform(y.ravel())
print('y: \n', y)

# modelo de classificação 
from sklearn.linear_model import LogisticRegression

# classificador
clf = LogisticRegression()
print(clf.fit(x, y))

# gerando 100 valores de temperatura
# linearmente espaçados entre 0 e 45
# predição em novos valores de temperatura
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

# predição desses valores
y_pred = clf.predict(x_test)
print(y_pred)

# conversão de y_pred Para os Valores Originais

y_pred = le.inverse_transform(y_pred)
print(y_pred)

print('\n***************************************\n')

# output
output = {'new_temp' : x_test.ravel(),
          'new_class' : y_pred.ravel()}
output = pd.DataFrame(output)

print('\n INFO: ',output.info(),'\n\n')
print(output)

# estatisticas
print('\n***************************************\n')

print(output.describe())


# contagem  de valores gerados
plt.figure(figsize=(10, 5))
plt.title('# novos valores gerados')
plt.plot(output['new_class'].value_counts())
plt.bar(output['new_class'], height=output['new_temp'])
plt.show()

# distribuição do output produzido 
# conseguimos inferir a classificação  novas temperaturas
# a Partir de um datase com 6 exemplos

plt.figure(figsize=(10, 5))
plt.plot(output['new_class'])
plt.boxplot(output['new_temp'])
plt.show()

# sistema automatico
def classify_temp():
    '''Classifica o input do usuario'''
    ask = True
    while ask:
        # input de temperatura
        temp = input('Insira a temperatura(Graus Celsius): ')

        # transforma para numpy array
        temp = np.array(float(temp)).reshape(-1, 1)

        # realiza Classificação 
        class_temp = clf.predict(temp)

        # transformação inversa para retornar  a string original
        class_temp = le.inverse_transform(class_temp)

        # classificação 
        print(f'A Classificação da temperatura {temp.ravel()[0]} é :', class_temp[0])

        # pergunta
        ask = input('Nova classificação (y/n): ') == 'y'

classify_temp()