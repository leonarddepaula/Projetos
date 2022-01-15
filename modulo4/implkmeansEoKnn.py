import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# crias dados aleatórios
dados = {'x':[25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],
        'y': [79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]
        }


# cria o dataframe
df = DataFrame(dados, columns=['x','y'])
print(df.head())
#print(df.info()) para descobrir o tamanho
#print(df.head(30)) iria printar todo o data


# Adicionar as bibliotecas para construir o algoritmo

Kmeans = KMeans(n_clusters=2) #cria o objeto de para o algoritimo K-means para encontrar 2 clusters
Kmeans.fit(df) # aplica o algoritmo
centroides = Kmeans.cluster_centers_ #encontra as condenadas dos centroids
print(centroides)

# Realizar o plot do Gráfico de Saída
plt.scatter(df['x'], df['y'], c= Kmeans.labels_.astype(float), s=50, alpha=0.5 )
plt.scatter(centroides[:, 0], centroides[:, 1], c='red', s=50)
plt.xlabel("x")
plt.ylabel("y")
plt.show()