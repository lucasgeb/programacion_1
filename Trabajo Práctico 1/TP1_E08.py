"""
ejercicio 8
El entrenador de un equipo de básquet desea determinar la eficiencia en tiros de campo
de un jugador "X".
"""

tiros_al_aro = int(input('ingrese cantidad de tiros realizados: '))
tiros_convertidos = int(input('ingrese cantidad de tiros convertidos '))

print("la eficiencia del jugador x es: ", tiros_convertidos / tiros_al_aro * 100)
