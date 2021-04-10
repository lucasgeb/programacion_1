
#! ejercicio 18.
#! Dado las tres cartas que representan una mano del truco, determinar si el jugador tiene
#! envido o no, en el caso de tener determinar cuántos puntos tiene (si tiene flor no puede
#! cantar envido).



carta1 = int(input('ingrese valor de la primer carta '))
palo1 = input('ingrese el palo de la carta 1 ')
carta2 = int(input('ingrese valor de la primer carta '))
palo2 = input('ingrese el palo de la carta 2 ')
carta3 = int(input('ingrese valor de la primer carta '))
palo3 = input('ingrese el palo de la carta 3 ')

if(palo1 == palo2 and palo1 == palo3):
    puntos = 20
    if(carta1 <= 7):
        puntos += carta1
    if(carta2 <= 7):
        puntos += carta2
    if(carta3 <= 7):
        puntos += carta3
    print('flor', puntos)
elif(palo1 == palo2 or palo1 == palo3 or palo2 == palo3):
    print("envido")