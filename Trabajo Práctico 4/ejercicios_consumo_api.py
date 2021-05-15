import json
import requests


def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data

def get_planet_by_id(id):
    data = get_docs("https://swapi.dev/api/planets/"+str(id))
    return data


def search_characters_by_name(name):
    data = get_docs("https://swapi.dev/api/people?search="+str(name))
    return data['results']

def get_all_sw_characters():

    sw_data = []

    data = get_docs("https://swapi.dev/api/people/")

    while(data["next"] is not None):
        for personaje in data["results"]:
            sw_data.append(personaje) #print(doc["name"], doc["url"][28:-1])
        data = get_docs(data["next"])
    
    return sw_data


def busqueda(data, buscado):
    pos = -1
    for index, personaje in enumerate(data):
        if(personaje["name"] == buscado):
            pos = index
    return pos



sw_data = get_all_sw_characters()

#! Mostrar toda la informacion de Yoda si esta en la Lista 

# buscado = "Yoda"

# posicion = busqueda(sw_data, buscado)

# if(posicion > -1):
#     print(buscado, "está en la lista en la posición", posicion)
#     print("info -->")
#     print(sw_data[posicion])
# else:
#     print(buscado, "no está en la lista")

#! Determinar si Mandalorian o Grogu esta en la lista

# buscado = "Grogu"

# posicion = busqueda(sw_data, buscado)

# if(posicion > -1):
#     print(buscado, "está en la lista en la posición", posicion)
#     print(sw_data[posicion])
# else:
#     print(buscado, "no está en la lista")


# buscado = "MandaLorian"

# posicion = busqueda(sw_data, buscado)

# if(posicion > -1):
#     print(buscado, "está en la lista en la posición", posicion)
#     print(sw_data[posicion])
# else:
#     print(buscado, "no está en la lista")

#! Mostrar todos los personajes con altura menor a 98 cm

# for character in sw_data:
#     if(character["height"].isdecimal()):
#         if(int(character["height"]) < 98):
#             print(character["name"], character["height"])

#! Mostrar todos los personajes con peso mayor a 100 kilos
# for character in sw_data:
#     if(character["mass"].isdecimal()):
#         if(int(character["mass"]) >= 100):
#             print(character["name"], character["mass"])

# sw_data = get_all_sw_characters()


#! Mostrar todos los personajes del planeta natal Tatooine y Coruscant
# for character in sw_data:
#     if (character ["homeworld"] == "http://swapi.dev/api/planets/1/"):
#         print( character ["name"], "  tatooine")
#     elif (character ["homeworld"] == "http://swapi.dev/api/planets/9/"):
#         print( character ["name"], "  Coruscant")



# #! Mostrar todos los personajes de especie Kaleesh y Kaminoan

# for character in sw_data:
#     if ("http://swapi.dev/api/species/32/" in character['species']):
#         print(character ["name"], character["species"])
#     elif ("http://swapi.dev/api/species/36/" in character['species']):
#         print(character ["name"], character["species"]) 


#! Mostrar toda la informacion del planeta Coruscant (9) y Kamino (10)


# data = get_planet_by_id(9) 
# print(data) 

# data = get_planet_by_id(10) 
# print(data) 

#! Mostrar toda la informacion de las naves usadas por Luke Skywalker

# for character in sw_data:

#     if("Luke Skywalker" in character['name']):
#         print(character ["name"], character["starships"]) 

#! Mostarr toda las peliculas en las que aparecio R2-D2
# for character in sw_data:
#     if("R2-D2" in character['name']):
#         print(character["name"], character["films"])

#! Mostrar el resumen de la introduccion (opening_crawl) del episodio 4 "A New Hope"