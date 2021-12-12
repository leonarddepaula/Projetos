# criando array na pratica aula 2.2
#importando as bibliotecas

import numpy as np

# ajuda do  metodo.
#help(np.array)  

#criação de um array AD:[1, 2, 3]
lista = [1, 2, 3]
x = np.array(lista)
print('x:',x)
print("shape: linhas + colunas ",x.shape) # fala a contidade de elementos em cada dimensao
print(type(x))

# Criando um Array 2D: listas aninhadas
lista = [[1, 2, 3], [2, 4, 6]]
x = np.array(lista)
print('x \n', x)
print('shape: linhas + colunas ', x.shape)

# array contendo apenas 0´s
#help(np.zeros)
dim = (3, 4)
x = np.zeros(dim)
print('x \n', x)
print('shape: ', x.shape)

# array contendo apenas  1´s
size = (2, 2) #(linhas, colunas)
x = np.ones(size)
print('x \n', x)
print('shape: linhas + colunas', x.shape)

# criação de valores dentro de um intervalo
# valores uniformes entre 5 e 15
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6) # cris posições aleatoreas entre (5, 15)
print('x \n', x)
print('shape: posições', x.shape)

# criação de matriz identidade
n = 4
x= np.eye(n)
print('x \n', x)
print('shape: linhas + colunas', x.shape)

# criação de valores aleatorios 
# np.random.seed(10)
x = np.random.random(size=(2, 3))
print('x \n', x)
print('shape: linhas + colunas', x.shape)