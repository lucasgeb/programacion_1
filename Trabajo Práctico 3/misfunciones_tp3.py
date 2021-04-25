def suma(numero1, numero2):
    """suma dos numeros"""
    return numero1 + numero2



def positivo_negativo(numero):
    """determina si el número es positivo(devuelve true) o negativo(devuelve false)"""
    if (numero >= 0):
        return True
    else:
        return False



def area_rectangulo(base, altura):
    """calcula el área del rectangulo multiplicando base por altura"""
    return base * altura


def contar_caracter(cadena, caracter):
    '''contar cuantas veces aparece el caracter en la cadena'''
    cantidad = 0
    for letra in cadena:
        if(letra == caracter):
            cantidad += 1
    return cantidad

def es_palíndromo(cadena):
    '''determina si una palabra es palindromo'''
    cadena_aux= list(cadena)
    cadena_aux.reverse()
    cadena_invertida = ""
    cadena_invertida = cadena_invertida.join(cadena_aux)
    return cadena_invertida == cadena


def sumatoria(numero):
    suma = 0
    for i in range(1, numero+1):
        suma += 1/i
    return suma


def calculo(operacion, numero1, numero2):
    "realizar una operación dada entre dos números"
    operacion
    if(operacion == "suma"):
        return numero1 + numero2
    elif(operacion == "resta"):
        return numero1 - numero2
    elif(operacion == "multiplicacion"):
        return numero1 * numero2
    else:
        return False


def numero_primo(numero):
    "determina si un numero es primo devuelve true) o no (devuelve false)"
    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            return True

def vocal(caracter):
    "determinar si un caracter es vocal"
  
    if(caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
        return caracter, "Es vocal"
    else:
        print("no es vocal")


def numero_mayor(numero1, numero2):
    "determina que numero es mayor"

    if(numero1 >= numero2):
        return "el primer número es mayor"
    else:
        return "el segundo número es mayor"


def intercambiar_variable(numero1, numero2):
    "intercambia el valor de dos variables"

    a = numero1
    b = numero2
    a, b = b, a
    return (a , b)

def aleatorio(numero1, numero2):
    "elije un numero aleatorio entre dos numeros dados"

    from random import randint

    return randint(numero1, numero2)