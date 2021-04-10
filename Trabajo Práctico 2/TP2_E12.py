
#! ejercicio 12
#! Dado un número de mes (de 1 a 12) determinar cuántos días tiene dicho mes

mes = int(input("Ingrese el número del 1 al 12 correspondiente al mes: "))

if(mes >= 1 and mes <12):
    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        print("el mes tiene 31 días")
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        print('el mes tiene 30 días')
    else:
        print("el mes tiene 28 días")
else:
    print("el mes no existe")