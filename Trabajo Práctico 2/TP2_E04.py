
"""
Ejercicio 4
Dada las tres notas obtenidas por un alumno en los distintos parciales, determinar si el
mismo está aprobado o desaprobado.
"""

nota_1 = float(input('ingrese la nota 1: '))
nota_2 = float(input('ingrese la nota 2: '))
nota_3 = float(input('ingrese la nota 3: '))

promedio_notas = round((nota_1 + nota_2 + nota_3) / 3, 2)

if(promedio_notas > 7):
    print("el alumno está aprobado")
else:
    print("derecho a marzo")

print('fin del algoritmo')