#base = int(input("ingrese la base del rectangulo"))
#altura = int(input("ingresa la altura del rectangulo"))
#
#area = base * altura

# print("el área del triangulo es ", area)

# precio_maquina = int(input('ingrese el valor de la maquina es USD '))
# cotizacion_dolar = int(input('ingrese el valor de la cotización actual del dolar '))

# valor_en_pesos = precio_maquina * cotizacion_dolar

# print('el valor de la máquina en pesos argentinos es ', valor_en_pesos)

# base = int(input('ingresar cuanto mide la base del triangulo en cm '))
# altura = int(input('ingresar cuanto mide la altura del triangulo en cm'))

# print("el área del triangulo es ", base * altura / 2 , 'cm')

# valor_hora = int(input("ingrese el valor del estacionamiento por hora "))
# tiempo_estacionado = int(input("ingrese el tiempo que el cliente estuvo estacionado"))

# valor_servicio = valor_hora * tiempo_estacionado

# print("el cliente debe pagar ", valor_servicio, 'pesos')

# costo_minuto = float(input("ingrese el costo del minuto de llamado "))
# tiempo_hablando = int(input(' ingrese los minutos que el cliente estuvo en llamada '))

# valor_servicio_telefonico = costo_minuto * tiempo_hablando

# print("el cliente debe pagar ", round(valor_servicio_telefonico * 1.005, 2))


# valor_kw = float(input("ingrese el costo del consumo por Kw/h "))
# consumo_hora = int(input("ingrese las horas que se utilizó el servicio "))

# costo_servicio = valor_kw * consumo_hora
# costo_mas_impuesto = costo_servicio * 1.0021
# valor_final_descuento = costo_mas_impuesto * 0.963

# print("el cliente debe pagar ", round(valor_final_descuento, 2), "pesos ")

# numero = int(input('ingrese un numero '))

# if(numero < 19):
#     print('el numero ingresado es menor que 19')
# else:
#     print("el numero ingresado es mayor que 19")


# numero = int(input('ingrese un numero '))

# if(numero > 0):
#     print('el numero es positivo')
# elif(numero < 0):
#     print('el numero es negativo')
# else:
#     print('el numero ingresado es 0')

# nota1 = float(input('ingrese la nota del primer parcial '))
# nota2 = float(input('ingrese la nota del segundo parcial '))
# nota3 = float(input('ingrese la nota del tercer parcial '))

# promedio = (nota1 + nota2 + nota3) / 3

# if(promedio >= 6):
#     print(round(promedio, 2),'el alumno aprobó la materia')
# else:
#     print(round(promedio,2),'el alumno no aprobo la materia')

# anio_actual = int(input('ingrese el año actual'))

# nombre_apellido1 = input('ingrese el nombre y apellido de la persona 1 ')
# anio_nac_1 = int(input('ingrese al año de nacimiento de la persona 1'))

# nombre_apellido2 = input('ingrese el nombre y apellido de la persona 2 ')
# anio_nac_2 = int(input('ingrese al año de nacimiento de la persona 2'))

# nombre_apellido3 = input('ingrese el nombre y apellido de la persona 3 ')
# anio_nac_3 = int(input('ingrese al año de nacimiento de la persona 3'))

# if(anio_actual - anio_nac_1 > 18):
#     print(nombre_apellido1, "es mayor de edad")

# if(anio_actual - anio_nac_2 > 18):
#     print(nombre_apellido2, "es mayor de edad")

# if(anio_actual - anio_nac_3 > 18):
#     print(nombre_apellido3, "es mayor de edad")


from random import randint

num_1 = randint(1,83)
num_2 = randint(1,83)

personaje_1 = get_charter_by_id(num_1)

personaje_2 = get_charter_by_id(num_2)

print("el primer personaje elegido al azar es: ", personaje_1['name'])
print("el segundo personaje elegido al azar es: ", personaje_2['name'])


#! comparar alturas de los personajes



if(altura(personaje_1) > altura(personaje_2)):
    print("personaje 1 es mas alto que personaje 2")
else:
    print("personaje 2 es mas alto")

#!  comparar pesos de los personajes


if(peso(personaje_1) > peso(personaje_2)):
    print("personaje 1 es mas pesado que personaje 2")
else:
    print("personaje 2 es mas pesado")

#! cual personaje participó en mas peliculas



#!determinar si alguno de los personajes aleatorios se llama Yoda o Grievous


if(personaje_1["name"] == "Yoda" or personaje_2["name"] == "Yoda"):
    print("uno de los personajes elegidos al azar es Yoda!")
elif(personaje_1["name"] == "Grievous" or personaje_2["name"] == "Grievous"):
    print("uno de los personajes elegidos al azar es Grievous")
else:
    print("ninguno de los personajes elegidos al azar es Yoda o Grievous")
