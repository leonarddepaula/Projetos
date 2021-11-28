# FUNÇÕES

# Def

def imc (peso, altura):
    imc = peso/(altura**2)
    if imc < 18.5:
        print('magreza')
    elif imc >= 18 and imc <= 24.9:
        print('Normal')
    elif imc >= 25.0 and imc <=29.9:
        print('sobrepeso')
    elif( imc >= 30.0 and imc <= 39.9):
        print('obesidade')
    else:
        print('obesidade grau II')
    return imc

print(imc(80, 1.94))

# return imc retora a condição e o valor 
# se chamar apenas o return ele retorna a condição 
# e um None ex: Normal 
              # Nome