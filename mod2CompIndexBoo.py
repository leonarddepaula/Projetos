'''
 comparação e indexação booleana

'''
import numpy as np

# criação de arrays
print('\n***Comparação***\n')
x = np.array([[1, 2], [3, 4]])
y = np.array([1.5, 3.5])
print('x: \n', x)
print('y: \n', y)

# Comparação ponto a Ponto.
print("comparação de um array com um escalar (>): \n", x > 2)
print("comparação de um array com um escalar (>=): \n", x >= 2)
print("comparação de um array com um escalar (<): \n", x < 2)
print("comparação de um array com um escalar (<=): \n", x <= 2)
print('comparação entre arrays (==): \n', x == x)
print('comparação entre arrays (>): \n', x > x)
print('comparação entre arrays (==): \n', x > y) #broadcasting

'''
INDEXAÇÃO BOOLEANA

'''
print('\n***Indexação Booleana***\n')

# indexação booleana
x= np.array([[1, 3, 7],
            [4, 11, 21],
            [42, 8, 9]])
print('x: \n', x)

# indexação booleana: retornar o numero de elementos.
# maiores que K
print('\n***Retornar o numero de elementos maiores que K***\n')
k = 10
cond = x > k #numeros pares
print("condição: \n", cond)
print(f"elementos maiores que {k}: ", x[cond])
print(f'números de elementos maiores que {k}: ',len(x[cond]))

# Extração de numeros pares
print('\n***EXTRAÇÃO DE NUMEROS PARES***\n')
cond = x % 2 == 0 #numeros pares
print('condição: \n', cond)
print('números pares: ', x[cond])


print('\n***EXTRAÇÃO DE NUMEROS IMPARES***\n')
cond = x % 2 == 1 #numeros Impares
print('condição: \n', cond)
print('números pares: ', x[cond])

