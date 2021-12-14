'''
outras operações Uteis em numpy

'''
import numpy as np 

# array
x = np.array([[1, 2, 3],
             [4, 11, 21],
             [42, 8, 9]])
# reshape: transformar a matriz em um vetor coluna
# (3, 3) vira (9, 1): 3*3 = 9*1 = 9
print("transformação de um vetor coluna: \n", x.reshape(9, 1))

# transpiração de matriz
print("x transporta: \n", x.T)


print('\n************************************\n')
# np.sum: soma em um dado eixo, axis = {0: linha, 1: coluna}
print('x:\n', x)
print("Soma de todos os Elementos de x: ", np.sum(x))
print("soma de x ao longo das linhas:", np.sum(x, axis=0))
print("soma de x ao longo das colunas:", np.sum(x, axis=1))

# np.mean: média em um dado eixo , axis = {0: linha, 1 : coluna}

print('\n************************************\n')
print("x: \n", x)
print('média de todos os elementos de x: ', np.mean(x))
print("média de x ao longo das linhas: ", np.mean(x, axis=0))
print('media de x ao longo das colunas: ', np.mean(x, axis=1))

# np.where, indenticação dos indices onde uma dada condição 
# é atendida. uso conjunto com indexação Booleana
cond = x % 2 == 0 
print('condição: \n', cond)
i, j = np.where(cond) # indices x[i, j ] = x[cond]
print('indice i (linhas: ', i)
print('indice j (colunas): ',j)

# indexação booleana e slicing: selecionar as linhas
#  de x que possuem algum numero par
print("x: \n", x)
cond = x % 2 == 0 # numeros pares
print("condição : \n", cond)


# se houver alguma condição  de true na linha , a soma será > 0 
i_row = np.where(np.sum(cond, axis=1)) [0]
print('indice das linhas que possuem números pares:', i_row)
print('linhas que possuem numeros pares: \n', x[i_row, :])