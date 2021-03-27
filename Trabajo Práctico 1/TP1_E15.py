"""
ejercicio 15
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