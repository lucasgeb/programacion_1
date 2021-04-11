"""
Ejercicio 15
Dado el valor numérico de la temperatura ambiente y su escala representada con una
carácter (C Celsius y F Fahrenheit), convertirla a la otra escala aplicando las siguientes
fórmulas según correspondan:
a. de F a C: (temp_f - 32) * 5/9
b. de C a F: (temp_c * 5/9) + 32
"""
temperatura = float(input('ingrese el valor de la temperatura '))
escala = input('ingrerse la escala C/F ')

if(escala == 'C'):
    print('la temperatura en grados Farenheit es', (temperatura * 9/5) + 32)
elif(escala == 'F'):
    print("la temperatura en grados celcius es", (temperatura - 32) * 9/5)
else:
    print('la escala ingresada es incorrecta')