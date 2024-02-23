class Cinema:
    def __init__(self, fileiras, assentos_por_fileira):
        self.fileiras = fileiras
        self.assentos_por_fileira = assentos_por_fileira
        self.mapa_assentos = [[False] * assentos_por_fileira for _ in range(fileiras)]

    def mostrar_mapa(self):
        print("Mapa de Assentos:")
        for i in range(self.fileiras):
            for j in range(self.assentos_por_fileira):
                print("X" if self.mapa_assentos[i][j] else ".", end=" ")
            print()

    def reservar_assento(self, fileira, assento):
        if fileira < 1 or fileira > self.fileiras or assento < 1 or assento > self.assentos_por_fileira:
            print("Assento inválido.")
            return False

        if self.mapa_assentos[fileira - 1][assento - 1]:
            print("Este assento já está reservado.")
            return False

        self.mapa_assentos[fileira - 1][assento - 1] = True
        print(f"Assento na fileira {fileira}, assento {assento} reservado com sucesso!")
        return True

# Função para o menu
def menu():
    print("\nOpções:")
    print("1. Ver mapa de assentos")
    print("2. Reservar um assento")
    print("3. Sair")

# Exemplo de uso:
cinema = Cinema(5, 10)

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cinema.mostrar_mapa()
    elif opcao == "2":
        fileira = int(input("Digite o número da fileira: "))
        assento = int(input("Digite o número do assento: "))
        cinema.reservar_assento(fileira, assento)
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
