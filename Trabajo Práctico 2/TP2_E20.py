"""
Ejercicio 20
Dado 5 números contar cuantos son múltiplos de 3.
"""
num1 = int(input('intrese un numero '))
num2 = int(input('intrese un numero '))
num3 = int(input('intrese un numero '))
num4 = int(input('intrese un numero '))
num5 = int(input('intrese un numero '))

cantidad_multiplos_3 = 0

if(num1 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num2 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num3 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num4 % 3 == 0):
    cantidad_multiplos_3 += 1
if(num5 % 3 == 0):
    cantidad_multiplos_3 += 1

print('la cantidad de multiplos de 3 es ', cantidad_multiplos_3)
