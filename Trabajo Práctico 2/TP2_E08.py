
"""
Ejercicio 8.
Ahora modifique el ejercicio anterior en el que además se conoce el número de cuotas en
la que paga, y aplicar los siguientes criterios para obtener el monto final (los recargos por
cuotas son los mismos para cualquier tarjeta):
a. Si paga en una cuota no hay recargo por cuotas
b. Si paga en tres cuotas el recargo es del 3 %
c. Si paga en ocho el recargo es del 17 %
d. Si paga en doce el recargo es del 32 %
"""

monto = float(input('ingrese el monto de la compra '))
tarjeta = input('ingrese tarjeta ')
cuotas = int(input('ingrese cantidad de cuotas '))

if(cuotas == 3):
    monto = monto * 1.03
elif(cuotas == 8):
    monto = monto * 1.17
elif(cuotas == 12):
    monto = monto * 1.32
else:
    monto = monto * 1.00


if(tarjeta == 'visa'):
    print("el monto es ", round(monto * 1.07, 2))
elif(tarjeta == 'mastercard'):
    print('el monto es ', round(monto * 1.11, 2))
else:
    print('el monto es ', round(monto, 2))