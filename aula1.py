def ePar(numero):
    if (numero%2)== 0:
        print("{} é par".format(numero))
    else:
        print("{} é impar".format(numero))
if __name__ ==" __main__":
    ePar(int(input("qual é o numero: ")))