
#! CICLOS - FUNCIONES Y MODULOS - ESTRUCTURAS DE DATOS - STRING

#! Array o vectores conjunto de valores unificados en una sola variable (estáticas)
#! en PY Listas dinámicas

# datos = [2, 4, 6, 0, 100, 34, 5, 6, 9, 2]
# print(datos)




# cadena = "   hola MUNDO desde python con VS code    "

# print(cadena.capitalize())
# print(cadena.title())
# print(cadena.upper())
# print(cadena.lower())
# print(cadena.replace("o", "r"))
# print(cadena.split())
# print(cadena.find("python"))
# print(len(cadena))


#la función split te recorta los espacios
 

 
# datos = [123, True, 23.6]

# nombre = input('ingrese nombre de persona ').capitalize()

# datos.append(nombre)
# datos.append("Ana")
# datos.append("Julieta")
# datos.insert(2, "mariano")
# # datos.sort()
# # datos.remove("Carlos")
# print(datos)



# datos = [2, 3, 4, 7, 0, 1, 56, 6]

#! Ciclos existen dos en PY .. while(condicionado) no sabemos hasta cuando se va a ejecutar, hay que decirle cuantas veces hay que ejecutar para que no siga infinito
#!  y for(finito) ya conozco y le digo cuanto se tiene que ejecutar.


# nombre = input("ingrese su  nombre ")

# while(nombre != '' and nombre != "carlos"):
#     print('hola', nombre)
#     nombre = input('ingrese su nombre ')

# for i in range(0, 5):
#     nombre = input('ingrese su  nombre ')
#     print(i, nombre)


# for numero in datos:
#     if(numero == 56):
#         print("56 esta en la lista")


#! ingresar 10 numeros e indicar los que son multiplos de 2 y de 3

# for i in range(0, 10):
#     numero = int(input('ingrese un numero '))
#     if(numero % 2 == 0 and numero % 3 == 0):
#         print("es múltiplo de 2 y de 3")

#!Dada una lista de 15 personas de las que se conoce nombre y edad, determinar cúantas son mayopres de eedad

# datos = []

 
# for i in range(0, 3):
#     nombre = input('ingrese su nombre ').capitalize()
#     anio_nacimiento = int(input('ingrese año de nacimiento '))

#     datos.append(nombre)

#     edad = 2021 - anio_nacimiento

#     if(edad >= 18):
#         print(nombre, "es mayor de edad")
#     else:
#         print("es menor de edad")


#! Ejercicio 4

#! Dada las notas de los 18 alumnos de un curso determinar cantidad de aprobados y
#! desaprobados, y además el promedio de nota de los aprobados.

# #! ACUMULADOR
# suma = 0
# #! CONTADOR
# aprobado = 0

# for i in range(0, 3):
#     nota = float(input("ingrese la nota del alumno "))

#     if(nota >= 6):
#         suma += nota
#         aprobado += 1
#         print("aprobó la materia")
#     else:
#         print("no aprobó la materia")
# print("el promedio es", suma/aprobado)
# print("la cantidad de alumnos aprobados es ", aprobado)
    

#! ejercicio 6
#! Dado 15 números indicar cuál es el mayor.

# maximo = int(input('ingrese un numero '))

# for i in range (0, 15):
#     numero = int(input('ingrese un numero '))

#     if(numero > maximo):
#         maximo = numero


# print("el maximo es", maximo)




# while(nombre != '' and nombre != "carlos"):
#     print('hola', nombre)
#     nombre = input('ingrese su nombre ')


#! 9. Dada una lista de números (finalizada en cero) determinar cuántos números positivos y
#! negativos hay en dicha lista.

# numero = int(input('ingrese un numero '))

# while(numero != 0):
#     if(numero > 0):
#         print("el numero es positivo")
#     else:
#         print("el numero es negativo")

# positivos = 0
# negativos = 0

# numero = int(input('ingrese un numero '))
# while(numero != 0):
#     if(numero > 0):
#         positivos += 1
#     else:
#         negativos += 1
    
#     numero = int(input('ingrese un numero '))

# print("cantidad de positivos ", positivos)
# print("cantidad de negativos ", negativos)


