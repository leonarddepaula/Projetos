nome = str(input("Digite seu nome: "))

peso = float(input("digite seu peso: "))

altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)



if(imc > 18.5 and imc <24.9 ):
    print("nome: ", nome)
    print("peso: ", peso)
    print("altura: ", altura)
    print("Abaixo Do Peso Normal.")
    
elif( imc > 25.0 and imc < 29.9):
    print("nome: ", nome)
    print("peso: ", peso)
    print("altura: ", altura)
    print("Peso Normal.")

elif(imc > 30.0 and imc <34.9):
    print("nome: ", nome)
    print("peso: ", peso)
    print("altura: ", altura)
    print("Obesidade Classe I.")

elif(imc > 35.0  and imc < 39.9):
    print("nome: ", nome)
    print("peso: ", peso)
    print("altura: ", altura)
    priint("Obesidade Classe II.")
else:
    print("nome: ", nome)
    print("peso: ", peso)
    print("altura: ", altura)
    print("Obesidader clase III.")