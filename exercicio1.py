'''
sabendo que a area de uma circuferencia é calculada 2pi *r ao quadrado, crie uma função para retornar a area da cicurferenia
pi =3,14
'''


def calcular_area_de_circunferencia(raio):
    pi=3.14
    return pi*raio**2


if __name__ == "__main__":
    print(calcular_area_de_circunferencia(float(input("digite o raio da circunferencia"))))
    



