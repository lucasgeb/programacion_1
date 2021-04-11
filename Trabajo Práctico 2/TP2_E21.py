"""
Ejercicio 21
Dado 5 números sumar los que son múltiplos de dos y obtener el promedio de estos
"""
num1 = int(input('intrese un numero '))
num2 = int(input('intrese un numero '))
num3 = int(input('intrese un numero '))
num4 = int(input('intrese un numero '))
num5 = int(input('intrese un numero '))

cantidad_multiplos_2 = 0
suma = 0

if(num1 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num1
if(num2 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num2
if(num3 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num3
if(num4 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num4
if(num5 % 2 == 0):
    cantidad_multiplos_2 += 1
    suma += num5

print('la cantidad de multiplos de 2 es ', cantidad_multiplos_2)
print('el promedio de los N° multiplos de 2 es: ', suma / cantidad_multiplos_2)