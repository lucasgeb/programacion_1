"""
ejercicio 9
Una empresa de transportes les cobra a sus pasajeros por kilómetros recorridos, y
necesita poder calcular el monto a cobrar a un cliente cuando se baja.
"""
costo_por_km = float(input('ingrese el precio por km recorrido: '))
km_recorridos = float(input('ingrese la kantidad de km recorridos por el cliente: '))

costo_viaje = round((costo_por_km * km_recorridos), 2)

print('el costo del viaje es: ', costo_viaje, "pesos")