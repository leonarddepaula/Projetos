# capitulo 6  - Condições , loops e Funções Parate II.

# WHILE
num = 1 
while num < 10:
    print(num)
    num += 1
print('\nwhile contando de 1 ate 9')
print('\n/********************************************/\n')

# BREAK
num = 1
while num < 12:
    print(num)
    if num == 6:
        break
    num += 1
print('\nwhile devecontrar de 1 a 11 mas foi colocada um break no 6')
print('\n/********************************************\n')

# CONTINUE
num = 0
while num  < 20:
    num += 1
    if num == 12:
        continue
    print(num)
print('\nwhile contando de 1 a 20 pois inicializou do 0 ')
print('\n/********************************************\n')

# RANGE utilizada para contagem de valores.
# range(inicio, termino,salto).

for i in range(1,11):
    print(i)

print('\n for in range de 1 ate 10')
print('\n/********************************************\n')

for y in range(0, 110, 10):
    print(y)


print('\n for in range de 0 ate 100 pulando de 10 em 10')
print('\n/********************************************\n')
# DEF
