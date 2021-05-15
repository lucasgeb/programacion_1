# 1. Utilizando la función get_charter_by_id consuma los datos de dos personajes de la
# api de Star Wars de manera aleatoria para resolver los siguiente:
# a. cual es el personaje más alto (indicar el nombre)
# b. cual es el personaje más pesado (indicar el nombre)
# c. cual personaje participó en más películas (si los dos participaron en la misma
# cantidad indicarlo) (indicar el nombre)
# d. determinar si alguno de los personajes aleatorios se llama Yoda o Grievous


import json
import requests
from random import randint

def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_all_sw_characters():

    sw_data = []

    data = get_docs("https://swapi.dev/api/people/")

    while(data["next"] is not None):
        for personaje in data["results"]:
            sw_data.append(personaje) #print(doc["name"], doc["url"][28:-1])
        data = get_docs(data["next"])
    
    return sw_data

sw_data = get_all_sw_characters()

def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data


num_1 = randint(1,83)
num_2 = randint(1,83)

personaje_1 = get_charter_by_id(num_1)

personaje_2 = get_charter_by_id(num_2)

print("el primer personaje elegido al azar es: ", personaje_1['name'])
print("el segundo personaje elegido al azar es: ", personaje_2['name'])


#! comparar alturas de los personajes

def altura(item):
    # print(item, type(item))
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return -1


if(altura(personaje_1) > altura(personaje_2)):
    print("personaje 1 es mas alto que personaje 2")
else:
    print("personaje 2 es mas alto")

#!  comparar pesos de los personajes

def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return -1

if(peso(personaje_1) > peso(personaje_2)):
    print("personaje 1 es mas pesado que personaje 2")
else:
    print("personaje 2 es mas pesado")

#! cual personaje participó en mas peliculas

if(len(personaje_1["films"]) > len(personaje_2["films"])):
    print("el primer personaje participó en mas peliculas")
elif(len(personaje_2["films"]) > len(personaje_1["films"])):
    print("el segundo personaje participó en mas peliculas")
else:
    print("ambos personajes actuaron en la misma")

#!determinar si alguno de los personajes aleatorios se llama Yoda o Grievous


if(personaje_1["name"] == "Yoda" or personaje_2["name"] == "Yoda"):
    print("uno de los personajes elegidos al azar es Yoda!")
elif(personaje_1["name"] == "Grievous" or personaje_2["name"] == "Grievous"):
    print("uno de los personajes elegidos al azar es Grievous")
else:
    print("ninguno de los personajes elegidos al azar es Yoda o Grievous")
