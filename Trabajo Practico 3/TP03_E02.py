
#!Desarrollar un algoritmo que determine si un número es positivo o negativo.


from misfunciones_tp3 import positivo_negativo

numero = int(input('ingrese un número'))

if(positivo_negativo(numero)):
    print('el numero es positivo')
else:
    print('el número es negativo')
