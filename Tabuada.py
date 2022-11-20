def tabuada():

    print("********CALCULADORA********")

    continuar = 1

    while continuar ==1:
        multiplicador = 1
        multiplicado = int(input("digite o valor para multiplicar:"))
        resultado = 0

        for multiplicador in range (11):
            resultado = multiplicado * multiplicador
            print(f"{multiplicador} * {multiplicado}=", resultado)
            multiplicador += 1

        print("Desenja fazer outra conta?")
        print("1 - SIM")
        print("2 - Não")
        continuar = int(input())

if(__name__ == "__main__"):
    tabuada()