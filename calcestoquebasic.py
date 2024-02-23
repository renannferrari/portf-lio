f1 = 12
o2 = 36
a3 = 15.8

termosaceitos = ('ovos', 'farinha', 'açucar')

while True:
    print("\nMenu:")
    print("1. Verificar estoque")
    print("2. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        var1 = input("O que o senhor gostaria de verificar se há em estoque hoje? ")
        if var1 == "farinha":
            print("O estoque atual de farinha é de:", f1, "quilos!")
        elif var1 == "ovos":
            print("O estoque atual de ovos é de:", o2, "unidades!")
        elif var1 == "açucar":
            print("O estoque atual de açúcar é de:", a3, "quilos!")
        elif var1 not in termosaceitos:
            print("Por favor, insira um termo aceito: ovos, farinha ou açucar.")
    elif escolha == "2":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
