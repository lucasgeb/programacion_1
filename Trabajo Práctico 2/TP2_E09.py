
"""
Ejercicio 9
Dado el nombre, apellido y año de nacimiento de tres personas mostrar los datos de los
que son mayores de edad.
"""

ano_actual = int(input('ingrese el año actual: '))

nombre_persona_1 = input('ingrese el nombre de la persona 1: ')
ano_persona_1 = int(input('ingrese año de nacimiento de la persona 1: '))

nombre_persona_2 = input('ingrese el nombre de la persona 2: ')
ano_persona_2 = int(input('ingrese año de nacimiento de la persona 2 '))

nombre_persona_3 = input('ingrese el nombre de la persona 3: ')
ano_persona_3 = int(input('ingrese año de nacimiento de la persona 3 '))

edad_persona_1 = ano_actual - ano_persona_1
edad_persona_2 = ano_actual - ano_persona_2
edad_persona_3 = ano_actual - ano_persona_3


if(edad_persona_1 >= 18):
    print(nombre_persona_1, 'es mayor de edad, tiene ', ano_actual - ano_persona_1, "años")
else:
    print(nombre_persona_1, 'no es mayor de edad' )
if(edad_persona_2 >= 18):
    print(nombre_persona_2, 'es mayor de edad, tiene ', ano_actual - ano_persona_2, "años")
else:
    print(nombre_persona_2, 'no es mayor de edad' )
if(edad_persona_3 >= 18):
    print(nombre_persona_3, 'es mayor de edad, tiene ', ano_actual - ano_persona_3, "años")
else:
    print(nombre_persona_3, 'no es mayor de edad' )
