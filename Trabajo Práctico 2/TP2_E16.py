
#! ejercicio 16
#! Dada una fecha en formato día/mes/año indicar la fecha del día siguiente.

dia = int(input('ingrese el día con formato DD'))
mes = int(input('ingrese el mes con formato MM'))
ano = int(input('ingrese el año con formato AAAA'))

if(mes >= 1 and mes <= 12):
    if(mes == 2)