import Calculadora
import Tabuada
import Potencia

print("*********************************")
print("*********Menu de seleção*********")
print("*********************************")

print ("Opções disponiveis:\n 1- Calculadora\n 2- Tabuada\n 3- Potencia")
op = int(input("Selecione uma Opção: "))

if op == 1:
    Calculadora.calc()
elif op == 2:
    Tabuada.tabuada()
elif op == 3:
    Potencia.potencia()