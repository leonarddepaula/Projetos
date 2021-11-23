
# LISTA(ARAYS)
print('\n/*************************************/\n')

frutas = ['banada', 'abacate', 'laranja', 'melancia', 'caju', 'abacaxi']

saldo_alunos = [500.00, 1200.00, 1000.00, 600.00, 50000.00]

num_pacientes = [25, 36, 50, 45, 22, 33, 89]

print(frutas)
print(saldo_alunos)
print(num_pacientes)

print('\n/*************************************/\n')

# Permite duplicados

frutas_duo = ['banada', 'abacate', 'laranja', 'melancia', 'caju', 'abacaxi', 'banada', 'abacate', 'laranja', 'melancia', 'caju', 'abacaxi']
print(frutas_duo)
print('\n/*************************************/\n')

# Calcular tamanho da lista

print('tamanho da lista: ',len(saldo_alunos))
print('tamanho da lista: ',len(frutas_duo))
print('\n/*************************************/\n')

# Uma Lista Pode Conter Diferente Tipos De Dados.

variados = [10, 2.5, 'python']
print(variados)
print('\n/*************************************/\n')

# Acessar um item Da Lista

print(frutas[2])
print('\n/*************************************/\n')

# Adicionando itens na lista

frutas.append('morango')
print(frutas)
print('\n/*************************************/\n')

# Unir listas

saldo_alunos.extend(num_pacientes)
print(saldo_alunos)


