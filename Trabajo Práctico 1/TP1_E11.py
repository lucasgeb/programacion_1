"""
ejercicio 11
Una empresa telefónica debe facturar el costo de las llamadas telefónicas a sus cliente
para esto les cobra por tiempo de llamada (por minuto) pero además le adiciona un 0,5 %
del monto total de la llamada.
"""

costo_llamada = float(input('valor del minuto en pesos: '))
minutos_hablados = float(input('cantidad de minutos hablados: '))

print('el valor del servicio es ', round(costo_llamada * minutos_hablados * 1.05, 2), 'pesos')