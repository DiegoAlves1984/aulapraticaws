def criarArquivo(texto):
    try:
        with open("mercado.txt", "r+") as arquivo:
            conteudo = arquivo.readlines()
            conteudo.append(texto + "\n")
            arquivo.close()
        arquivo = open("mercado.txt", "w")
        arquivo.writelines(conteudo)
        arquivo.close()               
    except Exception as e:
        print("falha ao abrir o arquivo: {}".format(e))

if __name__ == "__name__":
    texto = input("O que deseja gravar? ")
    criarArquivo(texto)
    