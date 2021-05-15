# Generar una lista de 77 números aleatoriamente resolver lo siguiente:
# a. indicar el valor menor
# b. indicar el valor mayor
# c. ordenar la lista de manera creciente y mostrar dichos valores
# d. eliminar de la lista los valores impares (o en su defecto hacer un barrido que
# solo muestre los pares)

from random import randint


lista = []

for i in range (0,78):
    numero = randint(1,1000)
    lista.append(numero)

lista.sort() 

print(lista)

print("el número menor es", lista[0])  

print("el número mayor es", lista[77]) 

for lista in range (0,78):
    if(lista% 2 == 0):
        print(lista)

