
#! ejercicio 7
#! # Dado el monto de la compra de un cliente y la tarjeta de crédito con la que paga
#! determinar el monto final de la compra considerando los siguientes criterios:
#! a. Si la tarjeta es Visa se debe aplicar un recargo del 7 %
#! b. Si la tarjeta es Mastercard se le aplica un recargo del 11%

monto = float(input('ingrese el monto de la compra '))
tarjeta = input('ingrese tarjeta ')

if(tarjeta == 'visa'):
    print("el monto es ", monto * 1.07)
elif(tarjeta == 'mastercard'):
    print('el monto es ', monto * 1.11)
else:
    print('el monto es ', monto)