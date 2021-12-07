#boleanos 
bool_1 =  5 != 7
bool_2 = 1 + 1 != 2
bool_3 = 3 + 3 == 9

print(bool_1)
print(bool_2)
print(bool_3)


#conceitos interresantes em for 
grupos = [['ana', 'maria, carlos'], ['arroz', 'feijao', 'cebola']]
for grupos in grupos:
    print(grupos)

numeros  = [2, 3, 4, 5, 6]
dobro = []

#conceito dobro  bem interresante.
for numeros in numeros:
    dobro.append(numeros * 2)
print(dobro)


# modulos
import random
lista_aleatoria = [random.randint(1, 100) for n in range(101)]
print(lista_aleatoria)