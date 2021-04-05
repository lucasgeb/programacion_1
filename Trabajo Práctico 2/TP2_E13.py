
#! ejercicio 13
#! Dado tres números obtener el mayor de estos.

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("ingrese el segundo número: "))
numero_3 = int(input('ingrese el tercer número: '))

if(numero_1 > numero_2 and numero_1 > numero_3):
    print("el número mayor es ", numero_1)
elif(numero_2 > numero_1 and numero_2 > numero_3):
    print("el número mayor es ", numero_2)
else:
    print(print("el número mayor es ", numero_3))