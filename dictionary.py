# DICTIONARY

cod_uf = {
    21 : 'Maranhão',
    22 : 'Piauí',
    23 : 'Ceará',
    24 : 'Rio grande Do Norte',
    25 : 'Paraíba',
    26 : 'Pernanbuco',
    27 : 'Alagoas',
    28 : 'Sergipe',
    29 : 'Bahia'}


print(type(cod_uf))
print(cod_uf)
print('\n/******************************/\n')

# Valores Ordenados.

print(cod_uf.values())
print('\n/******************************/\n')

# Duplicados Não São permitidos.

# Acessando os Valores.

print(cod_uf.get(29))
print(cod_uf.get(23))

print(cod_uf.keys())
print('\n/******************************/\n')

# Adicionando Novos Valores.

cod_uf[30] = 'Léo De Paula'
print(cod_uf)