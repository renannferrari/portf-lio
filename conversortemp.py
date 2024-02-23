def celsius_para_fahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheit_para_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

print("Bem-vindo ao Conversor de Temperatura!\n")

print("Escolha a operação desejada:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")

opcao = int(input("Qual operação você deseja realizar? "))

if opcao == 1:
    celsius = float(input("\nPor favor, insira a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius são {fahrenheit:.2f} graus Fahrenheit.")
elif opcao == 2:
    fahrenheit = float(input("\nPor favor, insira a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit são {celsius:.2f} graus Celsius.")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
