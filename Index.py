import Calculadora
import Tabuada
import Potencia
import Media

print("*********************************")
print("*********Menu de seleção*********")
print("*********************************")

print ("Opções disponiveis:\n 1- Calculadora\n 2- Tabuada\n 3- Potencia\n 4- Media")
op = int(input("Selecione uma Opção: "))

if op == 1:
    Calculadora.calc()
elif op == 2:
    Tabuada.tabuada()
elif op == 3:
    Potencia.potencia()
elif op == 4:
    Media.med()