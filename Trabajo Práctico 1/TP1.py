"""
ejercicio 1
calcular el área de un rectangulo
"""
base = int(input("colocar cuantos cm mide la base: "))
altura = int(input("colocar cuantosc cm mide la altura"))

print("el área del rectángulo es ", base * altura, "cm")



"""
ejercicio 2
Determinar el costo en pesos de comprar una máquina para un laboratorio "X Lab",
sabiendo que el precio de la misma es en dólares porque se debe comprar en china.

"""

valor_maquina = int(input("colocar valor de la maquina en pesos: "))
valor_dolar_actual = int(input("colocar cotización del dolar al día de hoy: "))
cantidad_maquinas = int(input("colocar cantidad de máquinas a comprar: "))

print("el valor de máquina en dolares es: ", valor_maquina * valor_dolar_actual * cantidad_maquinas)


"""
ejercicio 3
El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
nacimiento.
"""

anio_actual = int(input("ingrese el año actual: "))
fecha_nacimiento_postulante = int(input("ingrese fecha de nacimiento del postulante: "))

edad = anio_actual - fecha_nacimiento_postulante

print("el postulante tiene ", edad, "años")

"""
ejercicio 4
Calcular el área de un triángulo.
"""

base_triangulo = int(input("ingrese cuantos cm mide la base del triangulo: "))
altura_triangulo  = int(input("ingrese cuantos cm mide la altura del triangulo: "))

print("el área del triangulo es ", base_triangulo * altura_triangulo / 2, "cm")


"""
ejercicio 5
Determinar cuánto debe pagar el cliente de un estacionamiento, el precio se determina
por las horas que ocupo el estacionamiento.
"""

precio_estacionamiento_hora = int(input("precio del estacionamiento por hora"))
tiempo_estacionado = float(input("colocar horas que el cliente estuvo estacionado "))

print("el cliente debe pagar: ", precio_estacionamiento_hora * tiempo_estacionado, "pesos")


"""
ejercicio 6
Una pinturería debe elaborar el presupuesto para un cliente y necesita calcular el costo
total, este se deriva de la cantidad de pintura requerida y de la mano de obra, teniendo en
cuenta lo siguiente: se requiere un litro de pintura por m2 y el costo de mano de obra es
del 45 % del precio total de pintura.
"""

precio_pintura = float(input("coloque precio por litro de pintura: "))
m2_para_pintar = float(input("ingrese m2 que necesita pintar: "))

litros_pitura_necesarios = m2_para_pintar * 1
precio_m2_pintado = precio_pintura * m2_para_pintar
mano_obra = litros_pitura_necesarios * precio_pintura * 0.45

print("presupuesto de obra: ", precio_m2_pintado + mano_obra, "pesos")

"""
ejercicio 7
Se desea calcular cuántos metros se deben recorrer para atravesar una plaza en diagonal,
pero solo se conocen las distancia de las cuadras de ambos lados.
"""
from math import hypot

cuadra_A = float(input("ingrese cuantos metros mide la cuadra A"))
cuadra_B = float(input("ingrese cuantos metros mide la cuadra B"))

print(hypot(cuadra_A, cuadra_B))


"""
ejercicio 8
El entrenador de un equipo de básquet desea determinar la eficiencia en tiros de campo
de un jugador "X".
"""

tiros_al_aro = int(input('ingrese cantidad de tiros realizados: '))
tiros_convertidos = int(input('ingrese cantidad de tiros convertidos'))

print("la eficiencia del jugador x es: ", tiros_convertidos / tiros_al_aro * 100)

"""
ejercicio 9
Una empresa de transportes les cobra a sus pasajeros por kilómetros recorridos, y
necesita poder calcular el monto a cobrar a un cliente cuando se baja.
"""
costo_por_km = float(input('ingrese el precio por km recorrido: '))
km_recorridos = float(input('ingrese la kantidad de km recorridos por el cliente: '))

costo_viaje = round((costo_por_km * km_recorridos), 2)

print('el costo del viaje es: ', costo_viaje, "pesos")

"""
ejercicio 10
Determinar cuánto demora una persona en ir en bicicleta de un lugar a otros, suponiendo
que esta se mueve a una velocidad constante y se conocen la cantidad de kilómetros del
camino.
"""

distancia_recorrida = float(input('indicar la distancia recorrida en km: '))
velocidad = int(input('indicar la velocidad en km/h del ciclista: '))

print('el ciclista recorre la totalidad del camino en', round(distancia_recorrida / velocidad, 2), "horas")

"""
ejercicio 11
Una empresa telefónica debe facturar el costo de las llamadas telefónicas a sus cliente
para esto les cobra por tiempo de llamada (por minuto) pero además le adiciona un 0,5 %
del monto total de la llamada.
"""

costo_llamada = float(input('valor del minuto en pesos: '))
minutos_hablados = float(input('cantidad de minutos hablados: '))

print('el valor del servicio es ', round(costo_llamada * minutos_hablados * 1.05, 2), 'pesos')

"""
ejercicio 12
Una empresa distribuidora de energía le cobra a sus abonados el consumo de kW por
hora, pero además debe sumarle el 0,21 % de impuesto, pero actualmente todos los
cliente están dentro de un plan de promoción que les descuenta el 3,7 % del monto total a
pagar.
"""
costo_kw = float(input("valor en pesos del kw/h"))
kw_consumidos =float(input('cantidad de kw/h consumidos'))

total_con_impuesto = round(costo_kw * kw_consumidos * 0.21, 2)

total_a_pagar = round(total_con_impuesto * 0.963, 2)

print('con la promoción incluida debe pagar: ', total_a_pagar, 'pesos')



"""
ejercicio 13
Un supermercado está estableciendo el precio de venta para nuevos productos, de estos
productos desean generar el 27 % de ganancia.
"""

precio_costo_producto = float(input('colocar precio de costo del producto: '))

print("el precio de venta debe ser: ", round(precio_costo_producto * 1.27, 2), "pesos")


"""
ejercicio 14
Un profesor desea calcular el promedio de un alumno a lo largo de los cuatro parciales que
rindió.
"""

examen_1 = float(input('nota del examen 1: '))
examen_2 = float(input('nota del examen 2: '))
examen_3 = float(input('nota del examen 3: '))
examen_4 = float(input('nota del examen 4: '))

print("la nota final promediada del alumno es: ", round((examen_1 + examen_2 + examen_3 + examen_4) / 4, 2))

"""
ejercicio 5
Un grupo de amigos se hospedan en un hotel, y al momento de pagar se dividen los gastos
de la siguiente manera:
a. Iván paga el 40 %
b. German paga el 33 %
c. Esteban paga el 55 % de lo que pago Iván
d. Hernán paga el resto
"""
total_a_pagar = float(input("el total a pagar en pesos es: "))
ivan_paga = total_a_pagar * 0.4
german_paga = total_a_pagar * 0.33
esteban_paga = ivan_paga * 0.55
Hernan_paga = total_a_pagar - esteban_paga - german_paga - ivan_paga

print("Ivan paga ", ivan_paga, "German paga ", german_paga, "Esteban paga", esteban_paga, 'Hernan paga', Hernan_paga)


"""
ejercicio 16
Calcular el promedio de temperatura y presión recolectado por una estación
meteorológica en una semana, considerando que realiza solo una medición al día.
"""
from statistics import mean
temperatura_1 = float(input('ingrese temperatura día 1: '))
temperatura_2 = float(input('ingrese temperatura día 2: '))
temperatura_3 = float(input('ingrese temperatura día 3: '))
temperatura_4 = float(input('ingrese temperatura día 4: '))
temperatura_5 = float(input('ingrese temperatura día 5: '))
temperatura_6 = float(input('ingrese temperatura día 6: '))
temperatura_7 = float(input('ingrese temperatura día 7: '))

presion_1 = float(input('ingrese presion día 1: '))
presion_2 = float(input('ingrese presion día 2: '))
presion_3 = float(input('ingrese presion día 3: '))
presion_4 = float(input('ingrese presion día 4: '))
presion_5 = float(input('ingrese presion día 5: '))
presion_6 = float(input('ingrese presion día 6: '))
presion_7 = float(input('ingrese presion día 7: '))

promedio_temperatura = mean([temperatura_1, temperatura_2, temperatura_3, temperatura_4, temperatura_5, temperatura_6, temperatura_7])
promedio_presion = mean([presion_1, presion_2, presion_3, presion_4, presion_5, presion_6, presion_7])

print('el promedio semanal de temperatura es: ', round(promedio_temperatura, 2), 'el promedio semanal de presión es: ', round(promedio_presion))


"""
ejercicio 17
Convertir un valor entero de horas a segundos.

"""

hora = int(input('inserte horas a transformar en segundos: '))

segundos = hora * 3600

print ('la cantidad de hora/s son: ', segundos, "segundos")


"""
ejercicio 18
Dada las tres mediciones que se realizó un pluviómetro en un día, cada vez que el mismo
se vacía, determinar cuántos milímetros llovió ese día.

"""
medicion_1 = float(input('indique los mm de la primer medición: '))
medicion_2 = float(input('indique los mm de la segunda medición: '))
medicion_3 = float(input('indique los mm de la tercera medición: '))

medicion_total = medicion_1 + medicion_2 + medicion_3

print('hoy llovieron ', round(medicion_total, 2), "mm en total")
