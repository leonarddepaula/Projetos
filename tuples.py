# TUPLES.

print('\n/*************************************/\n')

frutas = ('banada', 'laranja', 'abacate', 'melancia', 'caju', 'abacaxi')

saldo_alunos = (500.00, 1200.00, 1000.00, 600.00, 50000.00)

num_pacientes = (25, 36, 50, 45, 22, 33, 89)

# Os Valores São indexados.

print(frutas[1])
print(frutas[1:4])
print('\n/*************************************/\n')

# Permite Duplicados.

saldo_alunos_dup = (500.00, 1200.00, 1000.00, 600.00, 50000.00)
print(saldo_alunos_dup)
print('\n/*************************************/\n')

# Juntas tuples.

tupla_junto = frutas + num_pacientes
print(tupla_junto)
print(type(tupla_junto))
print('\n/*************************************/\n')

# Contar valores repitidos em uma Tuple

num_pacientes_X = (25, 36, 50, 45, 22, 33, 89,25, 36, 50, 45, 22, 33, 8925, 36,
                50, 45, 22, 33, 8925, 36, 50, 45, 22, 33, 89,25, 36, 50, 45, 22, 33, 89,
                45, 22, 33, 89,25, 36, 50, 45, 22, 33, 8925, 36,
                50, 45, 22, 33, 8925, 36, 50, 45)

print(num_pacientes_X.count(45))
print('\n/*************************************/\n')
