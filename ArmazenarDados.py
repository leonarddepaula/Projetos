# Fundamentos em Python.
# capitulio 4 - amazenar dados
# [] coleção de dados
# [] list
# () tuples
# {} sets
# [] Dictionary

# LSTA * são mutaveis e editaveis

lista_compras = ['chocolate', 'pimenta', 'farinha']
peso_produto = [15,50,63,58]
altura = [1.65, 1.53, 1.85, 2.10]
lista = [15, 'palavra', 523, 'palavra', 256.20]
print(lista_compras)
print(lista_compras[1])
print('produto:',lista_compras[2], ' peso:', peso_produto[3], ' altura:',altura[0])

print('\n/*****************************/\n\n')
# tuples nao são mutaveis nem editaveis.

listas_comprasx = ('chocolate', 'peimenta', 'farinha')
peso_produtox = (15,50,63,58)
alturax = (1.65, 1.53, 1.85, 2.10)
listax = (15,'palavra', 523, 'palavra',256.20)

print(listas_comprasx)
print(listax)

print('\n/*****************************/\n\n')
# set é usado para armazenar varios itens em uma unica variavel.


listas_comprasy = {'chocolate', 'peimenta', 'farinha'}
peso_produtoy = {15,50,63,58}
alturay = {1.65, 1.53, 1.85, 2.10}
listay = {15,'palavra', 523, 'palavra',256.20}

print(listas_comprasy)
print(listay)

print('\n/*****************************/\n\n')

# Dictionary
curso_estudantes = {'José':'Python','Maria':'Java','João':'C++'}
print(curso_estudantes)