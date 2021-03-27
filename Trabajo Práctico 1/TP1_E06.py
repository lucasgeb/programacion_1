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
