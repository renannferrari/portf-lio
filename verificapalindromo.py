def verifica_palindromo(texto):
    # Normaliza o texto: converte para minúsculas e remove espaços em branco e pontuação
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")

    # Inverte o texto
    texto_invertido = texto[::-1]

    # Verifica se o texto original é igual ao texto invertido
    if texto == texto_invertido:
        return True
    else:
        return False

# Solicita ao usuário que insira uma palavra ou frase
palavra_frase = input("Por favor, insira uma palavra ou frase: ")

# Verifica se a palavra ou frase é um palíndromo
if verifica_palindromo(palavra_frase):
    print(f'"{palavra_frase}" é um palíndromo!')
else:
    print(f'"{palavra_frase}" não é um palíndromo.')
