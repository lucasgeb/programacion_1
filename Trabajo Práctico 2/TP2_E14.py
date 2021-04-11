"""
Ejercicio 14
Dada una fecha en formato día/mes determinar si la misma es correcta.
"""

dias = int(input("ingrese el día"))
mes = int(input("Ingrese el número del 1 al 12 correspondiente al mes: "))

if(mes == 2 and dias > 28):
    print("la fecha es incorrecta")
elif(mes == 2 and dias <= 28):
    print("la fecha es correcta")
elif(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dias > 31):
    print("la fecha es incorrecta")
elif(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dias <= 31):
    print('la fecha es correcta')
elif(mes == 4 or mes == 6 or mes == 9 or mes == 11 and dias > 30):
    print("la fecha es incorrecta")
else:
    print('la fecha es correcta')

