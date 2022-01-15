from sklearn import neighbors, datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# cria a rotina para utilizar o dataset Iris
iris = datasets.load_iris()

# Converte o banco de dados iris para o dataframe
df_iris = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['target'])
print(df_iris.head())
# print(df_iris.info())
# print(df_iris.shape) # numero de linhas e de colunas

# Trasforma os dados em array 
x = df_iris.iloc[:, :-1].values #dados de entrada
y = df_iris.iloc[:, 4].values # Saídas ou target

# realiza a divisão dos dados entre treinamento e teste
from sklearn.model_selection import train_test_split # função que realisa a divisão do dataset
x_train, x_test, y_train, Y_test = train_test_split(x, y, test_size=0.20) # divide 20% para teste

# realiza o processo de normalização dos dados
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() #objeto que normaliza os dados
scaler.fit(x_train) #realiza a normalização dos dados

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# Treinando o Modelo
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5) # utiliza a construção por meio de 5 vizinhos
classifier.fit(x_train, y_train) # aplica a classificação

# realiza a previsão
y_pred = classifier.predict(x_test)

# constroi a matriz de confusão para comparar o modelo criado
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(Y_test, y_pred))
print(classification_report(Y_test, y_pred))

# Realizar o plot da matriz de confusão
matriz_confusao = confusion_matrix(Y_test, y_pred)
from mlxtend.plotting import plot_confusion_matrix


fig, ax = plot_confusion_matrix(conf_mat=matriz_confusao)
plt.show()