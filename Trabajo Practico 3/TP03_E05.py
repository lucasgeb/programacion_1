
#! Desarrollar un algoritmo que determine si una palabra es un palíndromo.

from misfunciones_tp3 import es_palíndromo

palabra = input("ingrese una palabra ")

if(es_palíndromo(palabra)):
    print(palabra, "es palíndromo")
else:
    print(palabra, "no es palíndromo")