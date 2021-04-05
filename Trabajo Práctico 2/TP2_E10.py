
#! ejercicio 10
#!  Dado un número determinar si el mismo es múltiplo de 2 o de 5, de ser así mostrar dicho
#! número elevado al cubo

#* opcion 1
numero = int(input('ingrese un numero '))
if(numero % 2 == 0):
    print(numero ** 3)
elif(numero % 5 == 0):
    print(numero ** 3)
else:
    print('no es multiplo de 2 ni de 5')

#* opcion 2

# numero = int(input('ingrese un numero '))
# if(numero % 2 == 0 or numero % 5 == 0):
#     print(numero ** 3)
# else:
#     print(' el número no es multiplo de 2 ni de 5')