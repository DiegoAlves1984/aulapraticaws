def calcularAreaTriangulo(base, altura):

    area = (base*altura) / 2
    return area

if __name__ == "__main__":
    base = float(input("digite a base do triagulo: "))
    altura = float(input("digite a altura do triangulo: "))
    areatriangulo = calcularAreaTriangulo(base, altura)
    print("A area do triangulo é: ", areatriangulo)