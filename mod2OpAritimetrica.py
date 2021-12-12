import numpy as np

# CRIAÇÃO DE DOIS ARRAYS X E Y
print("\nCRIAÇÃO DE DOIS ARRAYS X E Y!!\n")
x = np.ones((2, 2))
y = np.eye(2)
print("x : \n", x)
print('y: \n', y)

# SOMA
print('\n***SOMA***\n')
print('soma de dois arrays: \n', x + y)
print('soma com float/int: \n', x + 2) #broadcasting (ADD  2 em todas as posições de X)

# SUBTRAÇÂO
print('\n***SUBTRAÇÃO***\n')
print('subtração de dois arrays:\n', x - y)
print('subtração com float/int:  \n', x -2) #broadcasting (subtrai 2 de todos os elementos de X)

# divisão 
print('\n***DIVISÃO***\n')
print('divisão  de dois arrrays: \n', x / y)
print('divisão com float/int: \n ', x / 2) # broadcasting

'''
quando o boradcasting não funciona!
np.array([1, 2, 3]) + np.array([1, 2])

* Dimensões diferentes array inconsistente.

** np.array([1, 2, 3]) + np.array([1, 2, 3])
    ^\ assim funcionaria pois tem as mesmas dimensoes.
    
    ***np.array([1, 2, 3]) + np.array([1]) 
       ^\ assim funcionaria pois adicionaria um 
       a todas as posições.
'''

# soma subtração e divisão
print('\n***SOMA SUBTRAÇÃO E DIVISÃO***\n')
print('combinação de operações: \n', (x + y) / (x-2))

