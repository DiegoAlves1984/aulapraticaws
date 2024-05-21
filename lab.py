import arquivo, os

sair = False

while sair == False:
    opcao = input("escolha uma opção:\n"
                  "1: Cadastrar item\n"
                  "2: Listar itens\n"
                  "3:Sair\n")
    if opcao == "1":
        item = input("Digite o item a ser adicionado: ")
        arquivo.criarArquivo(item)
    elif opcao == "2":
        print("Falta implementar")
    elif opcao == "3":
        sair = True
    else:
        print("Opção inválida")
    os.system('cls')
        
