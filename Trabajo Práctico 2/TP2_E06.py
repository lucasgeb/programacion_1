
#! ejercicio 6
#! Dado dos números determinar cuál es el mayor o si son iguales

numero_1 = int(input('ingrese el numero A '))
numero_2 = int(input('ingrese el numero B '))

# opcion 1
# if(numero_1 > numero_2):
#     print('el número A es mayor que el numero B')
# else:
#     if(numero_2 > numero_1):
#         print('el número B es mayor que el numero A')
#     else:
#         print("son iguales")
# print('fin del algoritmo')

# opcion 2
if(numero_1 > numero_2):
    print('el número A es mayor que el numero B')
elif    (numero_2 > numero_1):
        print('el número B es mayor que el numero A')
else:
    print("son iguales")
print('fin del algoritmo')