'''
Regressão linear

'''
# vizualização de dados
import matplotlib.pyplot as plt
import numpy as np


# Dados

x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111,
      0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]

y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657,
      1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]
# plot dos dados


plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

'''

Iremos estimar uma função de tipo: y = a*x + b
ou seja, devemos achar quais os valores de a e b
que melhor representam os dados.

Os valores reais de a e b são: (a, b): 2, 1

'''
# transformando para numpy e vetor coluna
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# adicionando bias: para estimar o termo b
x = np.hstack((x, np.ones(x.shape)))

# estimando a e b
beta = np.linalg.pinv(x).dot(y)
print('a estimado: ', beta[0][0])
print('b estimado: ',beta[1][0])

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, x.dot(beta), label='regressão linear')

# plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, x.dot(beta), label='regressão linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão linear com Numpy')
plt.grid()
plt.show()