"""
ejercicio 14
Un profesor desea calcular el promedio de un alumno a lo largo de los cuatro parciales que
rindió.
"""

examen_1 = float(input('nota del examen 1: '))
examen_2 = float(input('nota del examen 2: '))
examen_3 = float(input('nota del examen 3: '))
examen_4 = float(input('nota del examen 4: '))

print("la nota final promediada del alumno es: ", round((examen_1 + examen_2 + examen_3 + examen_4) / 4, 2))
