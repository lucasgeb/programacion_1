# Utilizando la función get_all_sw_characters consuma los datos de todos los
# personajes de SW y resuelva lo siguiente:
# a. Listado ordenado de manera creciente por nombre, mostrando nombre,
# especie y planeta natal
# b. Indicar los personajes que aparecieron en las 6 películas



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



#! a. Listado ordenado de manera creciente por nombre, mostrando nombre,
#! especie y planeta natal


sw_data = get_all_sw_characters()

def nombre(item):
    return item["name"]

sw_data.sort(key=nombre)


for index, personaje in enumerate(sw_data):
    print(personaje["name"], personaje["species"], personaje["homeworld"])


#! b. Indicar los personajes que aparecieron en las 6 películas


# así no anda
# for personaje in sw_data:
#     if ("http://swapi.dev/api/films/1/" and "http://swapi.dev/api/films/2/"  and "http://swapi.dev/api/films/3/"  and "http://swapi.dev/api/films/4/"  and "http://swapi.dev/api/films/5/"  and "http://swapi.dev/api/films/6/"  in personaje['films']):
#         print(personaje["name"], "estuvo en las 7 peliculas")

for personaje in sw_data:
    if(len(personaje["films"]) == 6):
        print(personaje["name"])