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