#!/usr/bin/ python

"""
ejercicio 5
Determinar cuánto debe pagar el cliente de un estacionamiento, el precio se determina
por las horas que ocupo el estacionamiento.
"""

precio_estacionamiento_hora = int(input("precio del estacionamiento por hora "))
tiempo_estacionado = float(input("colocar horas que el cliente estuvo estacionado "))

print("el cliente debe pagar: ", precio_estacionamiento_hora * tiempo_estacionado, "pesos")
