# LOOPs

# loop da vida.

print('Responda sim ou não para as perguntas!\n')

trabalho = input('Você deve trabalhar hoje? ')
dia = input('O dia está bonito? ')
preguica = input('você está com Preguiça? ')

if trabalho == 'sim':
    print('Bom trabalho!')
elif trabalho == 'nao':
    print('Aproveite o dia')

if dia == 'sim' and trabalho == 'nao':
    print('Aproveite para caminhar.')
elif dia == 'nao' and trabalho =='nao':
    print('aproveite e assita filmes.')

if preguica == 'sim' and trabalho == 'nao':
    print('Aproveite e durma mais.')
elif preguica == 'nao' and trabalho == 'nao':
    print('Que tal estudar Python?')


