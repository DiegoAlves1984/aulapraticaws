'''def corrigir_primeira_letra(frase):
    if not frase:
        return "Digite Aqui."
    frase_corrigida = frase[0].upper() + frase[1:] if frase[0].islower() else frase
    
    num_caracteres = len(frase)

    return frase_corrigida, num_caracteres

frase = input ("digite uma frase aqui: ")
frase_corrigida, num_caracteres = corrigir_primeira_letra(frase)
print("Frase corrigida:", frase_corrigida)
print("Numero de caracteres na frase:", num_caracteres)'''


def primeiraMaiuscula(frase):
    frase = frase[0].upper() + frase[1:]
    return frase, len(frase)
if __name__ == "__main__":
    frase =input("digite uma frase: ")
    frase_maiuscula, tamamho = primeiraMaiuscula(frase)
    print("O tamanho da frase é:{}".format(tamamho))
    print(frase_maiuscula)


    ''' trocar a letra inicial por maiucula e mostrar quantos caracteres'''
