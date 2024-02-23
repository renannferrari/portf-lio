def calcular_fatorial(numero):
    if numero < 0:
        return "Erro: o fatorial de números negativos não é definido."
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial


numero = int(input("Por favor, insira um número inteiro positivo: "))

resultado = calcular_fatorial(numero)

print(f"O fatorial de {numero} é {resultado}.")
