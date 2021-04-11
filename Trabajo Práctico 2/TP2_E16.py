"""
Ejercicio 16
Dada una fecha en formato día/mes/año indicar la fecha del día siguiente.
"""
#! consultar porque no me sale el cambio de año
#! resto de las fechas OK

dia = int(input('ingrese el día con formato DD '))
mes = int(input('ingrese el mes con formato MM '))
ano = int(input('ingrese el año con formato AAAA '))

if(mes >= 1 and mes <= 12):
    if(mes == 2):
         if(dia >= 1 and dia <= 28):
            if(dia == 28):
                dia = 1
                mes += 1
            else:
                dia += 1
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 30):
        if(dia == 30):
            dia = 1
            mes += 1
        else:
            dia += 1
    elif(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia > 31):
        if(dia == 31):
            dia = 1
            mes += 1
        elif(dia == 31 and mes == 12): 
            dia = 1
            mes = 1
            ano += 1
        else:
            dia += 1
    print(dia, "/", mes, "/", ano)
else:
    print("fecha incorrecta")