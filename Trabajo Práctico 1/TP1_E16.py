"""
ejercicio 16
Calcular el promedio de temperatura y presión recolectado por una estación
meteorológica en una semana, considerando que realiza solo una medición al día.
"""
from statistics import mean
temperatura_1 = float(input('ingrese temperatura día 1: '))
temperatura_2 = float(input('ingrese temperatura día 2: '))
temperatura_3 = float(input('ingrese temperatura día 3: '))
temperatura_4 = float(input('ingrese temperatura día 4: '))
temperatura_5 = float(input('ingrese temperatura día 5: '))
temperatura_6 = float(input('ingrese temperatura día 6: '))
temperatura_7 = float(input('ingrese temperatura día 7: '))

presion_1 = float(input('ingrese presion día 1: '))
presion_2 = float(input('ingrese presion día 2: '))
presion_3 = float(input('ingrese presion día 3: '))
presion_4 = float(input('ingrese presion día 4: '))
presion_5 = float(input('ingrese presion día 5: '))
presion_6 = float(input('ingrese presion día 6: '))
presion_7 = float(input('ingrese presion día 7: '))

promedio_temperatura = mean([temperatura_1, temperatura_2, temperatura_3, temperatura_4, temperatura_5, temperatura_6, temperatura_7])
promedio_presion = mean([presion_1, presion_2, presion_3, presion_4, presion_5, presion_6, presion_7])

print('el promedio semanal de temperatura es: ', round(promedio_temperatura, 2), 'el promedio semanal de presión es: ', round(promedio_presion))

