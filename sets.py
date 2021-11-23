# SET

cidade =  {'Belo Horizonte', 'Manaus', 'Fortaleza', 'Porto Alegre'}

print(type(cidade))
print(cidade)
print('\n/**************************************/\n')

# Não Permitem Valores Duplicados.

cidade_repet =  {'Belo Horizonte', 'Manaus', 'Fortaleza', 'Porto Alegre',
'Belo Horizonte', 'Manaus', 'Fortaleza', 'Porto Alegre',
'Belo Horizonte', 'Manaus', 'Fortaleza', 'Porto Alegre'}

print(cidade_repet)
print('\n/**************************************/\n')

# Checando Valores De um Set.

cidades = {'Belo Horizonte', 'Manaus', 'Fortaleza', 'Porto Alegre'}
numeros = {1, 2, 3, 55}

print('manaus' in cidades)
print('Manaus' in cidades)
print(3 in numeros)
print('\n/**************************************/\n')

# Adicionando item ao Set.

cidade.add('Natal')
print(cidade)
print('\n/**************************************/\n')

# Unindo Sets.

cidades_internacionais = {'toquio', 'Londres', 'Berlin', 'Paris'}
cidade.update(cidades_internacionais)
print(cidade)