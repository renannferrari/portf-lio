def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicita ao usuário que insira um número inteiro positivo
numero = int(input("Por favor, insira um número inteiro positivo: "))

# Verifica se o número é primo ou não
if verificar_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
