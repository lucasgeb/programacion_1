
#! ejercicio 14
#! Dada una fecha en formato día/mes determinar si la misma es correcta.

fecha_ok = input('ingrese la fecha en formato DD/MM correcta: ')
fecha_a_determinar = input('ingrese la fecha en formato DD/MM a corroborar ')

if(fecha_ok == fecha_a_determinar):
    print("la fecha es correcta")
else:
    print("la fecha es incorrecta")