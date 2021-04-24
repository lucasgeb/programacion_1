
#!3. Desarrollar un algoritmo para calcular el área de un rectángulo.

from misfunciones_tp3 import area_rectangulo

base = int(input('ingrese la base del triangulo en cm '))
altura = int(input("ingrese la altura del triangulo en cm "))


print("el área del triangulo es ", area_rectangulo(base, altura), "cm2")