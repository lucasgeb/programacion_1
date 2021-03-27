"""
ejercicio 2
Determinar el costo en pesos de comprar una máquina para un laboratorio "X Lab",
sabiendo que el precio de la misma es en dólares porque se debe comprar en china.

"""

valor_maquina = int(input("colocar valor de la maquina en pesos: "))
valor_dolar_actual = int(input("colocar cotización del dolar al día de hoy: "))
cantidad_maquinas = int(input("colocar cantidad de máquinas a comprar: "))

print("el valor de máquina en dolares es: ", valor_maquina * valor_dolar_actual * cantidad_maquinas)
