
#!Desarrollar un algoritmo que simule una calculadora donde se le da como entrada dos
#!números y el tipo de operación y esta devuelve el resultado.

from misfunciones_tp3 import calculo 

operacion = input('operacion a realizar ')
numero1 = int(input('inserte numero 1 '))
numero2 = int(input('inserte numero 2 '))


print(calculo(operacion,numero1, numero2))