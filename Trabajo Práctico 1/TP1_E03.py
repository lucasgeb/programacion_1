"""
ejercicio 3
El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
nacimiento.
"""

anio_actual = int(input("ingrese el año actual: "))
fecha_nacimiento_postulante = int(input("ingrese fecha de nacimiento del postulante: "))

edad = anio_actual - fecha_nacimiento_postulante

print("el postulante tiene ", edad, "años")