"""
ejercicio 10
Determinar cuánto demora una persona en ir en bicicleta de un lugar a otros, suponiendo
que esta se mueve a una velocidad constante y se conocen la cantidad de kilómetros del
camino.
"""

distancia_recorrida = float(input('indicar la distancia recorrida en km: '))
velocidad = int(input('indicar la velocidad en km/h del ciclista: '))

print('el ciclista recorre la totalidad del camino en', round(distancia_recorrida / velocidad, 2), "horas")
