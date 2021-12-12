# idexação de arrays
'''
Relembrando :
Os índices ao longo de uma dimensão variam de 0 an-1,
onde o n é o numero de elementos da dimensão.

'''
# os indices no python vão de 0 a -n,
# on n é o tamanho da dimensão.
import numpy as np

x = np.linspace(start=10, stop=100, num=10) # vai pegar 10 numeros aleatorioas entre 10 e 100.
print('\nx: ', x)
print('shape: ', x.shape)

# extração de elementos
print('\n***EXTRAÇÃO DE ELEMENTOS***\n')
print('x: ', x)
print("primeiro elemento: ",x[0])
print('Segundo elemento: ',x[1])
print("penultimo elemento: ",x[-2])
print("ultimo elemento: ",x[-1])

# slicing: extração de subarrays:
print('\n***SLICING: EXTRAÇÃO DE SUBARRAYS***\n')
print("x: ",x)
print("dois primeiros elementos: ", x[0:2])
print("dois primeiros elementos: ", x[:2])
print("dois ultimos elementos: ", x[-2:])

# slicing em arrays 2D(matrizes)
print('\n***SLICING EM ARRAYS 2D***\n')
x = x.reshape(2, 5)  # reshape de x para 2 linhas e 5 colunas
print("x:\n", x)

# extração de elementos (matriz)
# vai acessar os elementos criados no array 2d
print('\n***EXTRAÇÃO DE ELEMENTOS***\n')
print('primeira linha , segunda coluna: ', x[0, 1])
print('segunda linha, penultima coluna: ', x[1, -2])
print('ultima linha, ultima coluna: ', x[1, 4])
print('ultima linha, ultima coluna: ',x[-1, -1])

# slicing: extração de subarrays em 2d
print('\n***SLICING EXTRAÇÃO DE SUBARRAYS EM 2D***\n')
print("x: \n",x)
print('\nprimeira linha inteira: ',x[0, :])
print('primeira linha, segunda a quarta coluna: ',x[0, 1:4])
print('ultima coluna inteira:\n ', x[:, [-1]])

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print("x antes: ", x)
y = x[:2]
y[0] = -100 # aletração do valor em y altera o valor de x
print('depois: ',x)

# atenção com compartilhamento de memória em subarrays!!
x = np.array([1, 2, 3])
print("x antes: ", x)
y = x[:2].copy()
y[0] = -100 # aletração do valor em y altera o valor de x
print('depois: ',x)