import re

def verificar_senha_segura(senha):
    # Verifica o comprimento da senha
    if len(senha) < 8:
        return False
    
    # Verifica se há pelo menos uma letra maiúscula
    if not re.search("[A-Z]", senha):
        return False
    
    # Verifica se há pelo menos uma letra minúscula
    if not re.search("[a-z]", senha):
        return False
    
    # Verifica se há pelo menos um dígito
    if not re.search("[0-9]", senha):
        return False
    
    # Verifica se há pelo menos um caractere especial
    if not re.search("[!@#$%^&*()-+=]", senha):
        return False
    
    return True

# Solicita ao usuário que insira uma senha
senha = input("Por favor, insira sua senha: ")

# Verifica se a senha é segura ou não
if verificar_senha_segura(senha):
    print("A senha é considerada segura.")
else:
    print("A senha não atende aos critérios de segurança.")
