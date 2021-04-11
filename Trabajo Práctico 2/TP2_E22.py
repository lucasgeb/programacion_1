"""
Ejercicio 22
Simular que una persona tira tres veces un dado de seis lados (de manera aleatoria),
determinar si la persona saco un 5 y cuantos suma el total de los tres tiros.
"""
#!consultar, siempre sale que sacó 5

tiro_1 = int(input("ingrese el valor del dado del primer tiro: "))
tiro_2 = int(input("ingrese el valor del dado del segundo tiro: "))
tiro_3 = int(input("ingrese el valor del dado del tercer tiro: "))

if(tiro_1 or tiro_2 or tiro_3 == 5):
    print("la persona sacó al menos un 5")
else:
    print("la persona no sacó un 5")
print("la suma total de los tres tiros es ", tiro_1 + tiro_2 + tiro_3)