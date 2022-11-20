def potencia():
    print("********Potenciação********")

    continuar = 1

    while continuar ==1:

        print("digite dois valores:")
        valor1 = int(input("digite o primeiro valor: "))
        valor2 = int(input("digite o segundo valor: "))
        resultado = valor1 ** valor2
        
        print (f"O valor de {valor1} elevado a {valor2} é igual a {resultado}")

        print("deseja continuar?")
        print("1 => Sim")
        print("2 => Não")
        continuar = int(input())

if(__name__ == "__main__"):
    potencia()