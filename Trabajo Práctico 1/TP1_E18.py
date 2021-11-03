"""
ejercicio 18
Dada las tres mediciones que se realizó un pluviómetro en un día, cada vez que el mismo
se vacía, determinar cuántos milímetros llovió ese día  cambio

"""
medicion_1 = float(input('indique los mm de la primer medición: '))
medicion_2 = float(input('indique los mm de la segunda medición: '))
medicion_3 = float(input('indique los mm de la tercera medición: '))

medicion_total = medicion_1 + medicion_2 + medicion_3

print('hoy llovieron ', round(medicion_total, 2), "mm en total")