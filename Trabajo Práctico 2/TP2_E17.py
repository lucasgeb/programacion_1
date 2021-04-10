
#! ejercicio 17
#! Dado dos números mostrar la diferencia entre el mayor y el menor.

numero_1 = float(input("ingrese el primer número: "))
numero_2 = float(input("ingrese el segundo número: "))

if(numero_1 > numero_2):
    print("la diferencia es ", numero_1 - numero_2)
elif(numero_1 < numero_2):
    print("la diferencia es ", numero_2 - numero_1)
else:
    print("los números son iguales, no hay diferencia")
    