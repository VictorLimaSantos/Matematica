def med():
    print("********Média********")
    print("Calcule a Média das notas")
    nota1 = float(input("Digite a nota do primeiro bimestre: "))
    nota2 = float(input("Digite a nota do segundo bimestre: "))
    nota3 = float(input("Digite a nota do terceiro bimestre: "))
    nota4 = float(input("Digite a nota do quarto bimestre: "))
    resultado = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A méida final é igual a {resultado:.2f}" )
if(__name__ == "__main__"):
    med()