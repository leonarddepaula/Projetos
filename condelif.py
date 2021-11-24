# [] O que São funçoes, condiçoes e Loops em Python?

# if

# elipf

idade = int(input('Digite a sua idade: '))
if idade >= 18:
    print('Voce ja pode dirigir!')
elif idade < 18:
    print('voce ainda Nao pode Dirigir!')
elif idade >= 65:
    print('renove sua hablitação.')

print('\n//**************************************/\n')

exercicio = int(input('Quantos minutos voce se exercita por dia: '))

if exercicio < 30:
    print('Voce deveria se exercitar mais!')
elif exercicio >=30 and exercicio <= 60:
    print('voce esta no caminho certo!')
elif exercicio > 60 and exercicio <= 120:
    print('voce é um Atleta!')
else:
    print('Voce é foda!')
