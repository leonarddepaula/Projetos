def imc(peso, altura):
    print(peso / altura ** 2)

def saudacao(nome):
    print('Olá', nome, 'tudo bem?')

print('\n/*****************************/\n')

imc(80, 1.65)
print(imc)    
saudacao('roberto')
print(saudacao)

print('\n/*****************************/\n')

num = 0
while num < 20:
    print(num)
    num += 1
print('\n/*****************************/\n')

for i in range(0, 10, 2):
    print(i)
print('\n/*****************************/\n')

numeros = [1,2,3,4,5,6,7,8,9,10]
for x in numeros:
    print(x)
    if x == 3:
     break
print('\n/*****************************/\n')

num = 0
while num < 10:
    num += 1
    if num == 6:
        continue
