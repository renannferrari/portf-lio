import hashlib

class SistemaLogin:
    def __init__(self):
        self.usuarios = {}  # Dicionário para armazenar os usuários e senhas criptografadas

    def registrar_usuario(self, usuario, senha):
        if usuario not in self.usuarios:
            # Criptografar a senha antes de armazená-la
            hashed_password = hashlib.sha256(senha.encode()).hexdigest()
            self.usuarios[usuario] = hashed_password
            print("Usuário registrado com sucesso!")
        else:
            print("Este nome de usuário já está em uso. Tente outro.")

    def login(self, usuario, senha):
        if usuario in self.usuarios and self.usuarios[usuario] == hashlib.sha256(senha.encode()).hexdigest():
            print("Login bem-sucedido!")
        else:
            print("Nome de usuário ou senha incorretos.")

# Função para o menu
def menu():
    print("\nOpções:")
    print("1. Registrar novo usuário")
    print("2. Fazer login")
    print("3. Sair")

# Exemplo de uso:
sistema = SistemaLogin()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        usuario = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        sistema.registrar_usuario(usuario, senha)
    elif opcao == "2":
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        sistema.login(usuario, senha)
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
