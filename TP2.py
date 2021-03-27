"""
23/03/21
estructuras de control
El objetivo es llevar adelante el control de flujo de mi algortimo.´

estructuras condicionales (se ejecutan si se cumple una condición)
estructuras de control cíclicas (para repetir muchas veces)

Uso de funciones, reutilizar el código en momentos diferentes.
---------------------------
Estructuras condicionales:
- CONDICIONAL SIMPLE
- CONDICIONAL COMPUESTO
- CONDICIONAL ANIDADO


una condicion es una combinación con la siguiente estructura
valor|variable   operador_control   valor|variable

operadores de control: 
> mayor,
< menor, 
>= mayor o igual,
<= menor o igual,
== igual,
!= distinto

la tabulación de 4 espacios te da la rama verdadera
/ division
// division entera


Operadores lógicos
AND (y)
OR (ó)
XOR (uno o el otro)
NOT (no)

nos permiten agrupar condiciones
por ej. condicion_1 and condicion_2 - condicion_1 or condicion_2


"""

#! Ejercicio 1 
#! Dado un número determinar si es menor que 19.

# numero = int(input('ingrese un numero '))
# if(numero < 19):
#     print("el numero es menor que 19")
# else:
#     print('el numero es mayor')

# print('fin del algoritmo')


#! ejercicio 2
#! Determinar si un número dado es positivo o negativo.

# numero = int(input('ingrese un numero '))
# if(numero > 0):
#     print("el numero es positivo")
# else:
#     print("el numero es negativo")

#! ejercicio 3
#!  Determinar si un número dado es par o impar

# numero = int(input(' ingrese un numero '))

# if(numero % 2 == 0):
#     print('el número es par')
# else:
#     print('el número es impar')

# print("fin del algoritmo")

#! ejercicio 4
#! Dada las tres notas obtenidas por un alumno en los distintos parciales, determinar si el
#! mismo está aprobado o desaprobado.

# nota_1 = float(input('ingrese la nota 1: '))
# nota_2 = float(input('ingrese la nota 2: '))
# nota_3 = float(input('ingrese la nota 3: '))

# promedio_notas = round((nota_1 + nota_2 + nota_3) / 3, 2)

# if(promedio_notas > 7):
#     print("el alumno está aprobado")
# else:
#     print("derecho a marzo")

# print('fin del algoritmo')

#! ejercicio 5
#! Resuelva el ejercicio de 3 de la guía uno aplicando el filtro para los CV.

#! El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
#! vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
#! nacimiento.

# ano_actual = int(input("ingrese año actual "))
# ano_nacimiento = int(input('ingrese año de nacimiento del postulante '))

# ano_postulante = ano_actual - ano_nacimiento

# if(ano_postulante >= 18):
#     print('cumple con los requisitos de edad')
# else:
#     print('no comple con los requisitos de edad')
# print('fin del algoritmo')


#! ejercicio 6
#! Dado dos números determinar cuál es el mayor o si son iguales

# numero_1 = int(input('ingrese el numero A '))
# numero_2 = int(input('ingrese el numero B '))

# # opcion 1
# # if(numero_1 > numero_2):
# #     print('el número A es mayor que el numero B')
# # else:
# #     if(numero_2 > numero_1):
# #         print('el número B es mayor que el numero A')
# #     else:
# #         print("son iguales")
# # print('fin del algoritmo')

# # opcion 2
# if(numero_1 > numero_2):
#     print('el número A es mayor que el numero B')
# elif    (numero_2 > numero_1):
#         print('el número B es mayor que el numero A')
# else:
#     print("son iguales")
# print('fin del algoritmo')

#! ejercicio 7
#! # Dado el monto de la compra de un cliente y la tarjeta de crédito con la que paga
#! determinar el monto final de la compra considerando los siguientes criterios:
#! a. Si la tarjeta es Visa se debe aplicar un recargo del 7 %
#! b. Si la tarjeta es Mastercard se le aplica un recargo del 11%

# monto = float(input('ingrese el monto de la compra '))
# tarjeta = input('ingrese tarjeta ')

# if(tarjeta == 'visa'):
#     print("el monto es ", monto * 1.07)
# elif(tarjeta == 'mastercard'):
#     print('el monto es ', monto * 1.11)
# else:
#     print('el monto es ', monto)

#! 8. Ahora modifique el ejercicio anterior en el que además se conoce el número de cuotas en
#! la que paga, y aplicar los siguientes criterios para obtener el monto final (los recargos por
#! cuotas son los mismos para cualquier tarjeta):
#! a. Si paga en una cuota no hay recargo por cuotas
#! b. Si paga en tres cuotas el recargo es del 3 %
#! c. Si paga en ocho el recargo es del 17 %
#! d. Si paga en doce el recargo es del 32 %


monto = float(input('ingrese el monto de la compra '))
tarjeta = input('ingrese tarjeta ')
cuotas = int(input('ingrese cantidad de cuotas '))

if(cuotas == 3):
    monto = monto * 1.03
elif(cuotas == 8):
    monto = monto * 1.17
elif(cuotas == 12):
    monto = monto * 1.32
else:
    monto = monto * 1.00


if(tarjeta == 'visa'):
    print("el monto es ", monto * 1.07)
elif(tarjeta == 'mastercard'):
    print('el monto es ', monto * 1.11)
else:
    print('el monto es ', monto)


#! ejercicio 10
#!  Dado un número determinar si el mismo es múltiplo de 2 o de 5, de ser así mostrar dicho
#! número elevado al cubo

#* opcion 1
# numero = int(input('ingrese un numero '))
# if(numero % 2 == 0):
#     print(numero ** 3)
# elif(numero % 5 == 0):
#     print(numero ** 3)
# else:
#     print('no es multiplo de 2 ni de 5')

#* opcion 2

# numero = int(input('ingrese un numero '))
# if(numero % 2 == 0 or numero % 5 == 0):
#     print(numero ** 3)
# else:
#     print(' el número no es multiplo de 2 ni de 5')

#! ejercicio 11
#! Determinar si un número está dentro del rango de -15 hasta 81

# numero = int(input("ingrese un numero"))

# if( numero >= -15 and numero <= 81):
#     print('el numero está dentro del rango buscado')
# else:
#     print('el numero no está dentro del rango buscado')

#! ejercicio 12
#! Dado un número de mes (de 1 a 12) determinar cuántos días tiene dicho mes