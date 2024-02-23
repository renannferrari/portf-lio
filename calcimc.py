varpeso = float(input('Por favor, insira seu peso (em kg): ').replace(',', '.'))
varaltura = float(input('Por favor, insira sua altura (em metros): ').replace(',', '.'))

imc = varpeso / (varaltura ** 2)

print("Seu IMC é:", imc)

if imc <= 18.5:
    print('Você está abaixo do peso')
elif imc <= 24.9:
    print('Você está com o peso normal')
elif imc <= 29.9:
    print('Você está com sobrepeso')
elif imc <= 34.9:
    print('Você está com obesidade Grau I (leve)')
elif imc <= 39.9:
    print('Você está com obesidade Grau II (moderada)')
else:
    print('Você está com obesidade Grau III (grave)')
