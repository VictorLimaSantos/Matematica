def calc():
    print("********CALCULADORA********")

    continuar = 1

    while continuar ==1:

        print("digite dois valores:")
        valor1 = int(input("digite o primeiro valor"))
        valor2 = int(input("digite o segundo valor"))

        print("1) Soma")
        print("2) Subtração")
        print("3) multiplicação")
        print("4) Divisão")

        opcao = int(input("escolha uma opção:"))

        if opcao == 1:
            print(f"A soma de {valor1} + {valor2} =", valor1 + valor2)
        elif opcao == 2:
            print(f"A Subtração de {valor1} - {valor2} =", valor1 - valor2)
        elif opcao == 3:
            print(f"A multiplicação de {valor1} * {valor2} =", valor1 * valor2)
        elif opcao == 4:
            print(f"A Divisão de {valor1} / {valor2} =", valor1 / valor2)
        else:
            print("opção invalida")
            pass

        print("deseja continuar?")
        print("1 => Sim")
        print("2 => Não")
        continuar = int(input())

if(__name__ == "__main__"):
    calc()