"""
ejercicio 7
Se desea calcular cuántos metros se deben recorrer para atravesar una plaza en diagonal,
pero solo se conocen las distancia de las cuadras de ambos lados.
"""
from math import hypot

cuadra_A = float(input("ingrese cuantos metros mide la cuadra A "))
cuadra_B = float(input("ingrese cuantos metros mide la cuadra B "))

print(hypot(cuadra_A, cuadra_B))