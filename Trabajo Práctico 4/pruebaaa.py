import json
import requests


# def busqueda(data, buscado):
#     pos = -1
#     for index, personaje in enumerate(data):
#         if(personaje["name"] == buscado):
#             pos = index
#     return pos

from consumo_api import get_all_sw_characters

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

# def get_planet_by_id(id):
#     data = get_docs("https://swapi.dev/api/homeworld"+str(id))
#     return data

# for character in sw_data:
# data = get_planet_by_id(9) 
# print(data) 

# for character in sw_data:

# data = get_planet_by_id(10) 
# print(data) 

#! Mostrar toda la informacion de las naves usadas por Luke Skywalker


#! Calcular el promedio de altura de todos los personajes (acumulador, contador)

# def altura(item):
#     # print(item, type(item))
#     if(item['height'].isdecimal()):
#         return int(item['height'])
#     else:
#         return 0

# altura_personajes= 0
# personajes = 80

# for character in sw_data:
#    altura_personajes += altura(character)
# print(altura_personajes/personajes)



#! Calcular el peso promedio de los personajes especie humanos (acumulador especie, contador)
/# def peso(item):
#     if(item['mass'].isdecimal()):
#         return float(item['mass'])
#     else:
#         return 0

# peso_personajes_humano= 0
# personajes_humano = 0

# for character in sw_data:
#    if ("http://swapi.dev/api/species/1/" in character['species']):
#     peso_personajes_humano += peso(character)
#     personajes_humano += 1
# print("el peso promedio de los humanos es: ", peso_personajes_humano/personajes_humano)


#! Contar cuantos personajes especie droides y humanos hay (contador y contador)

personaje_droide = 0
personaje_humano = 0

for character in sw_data:
   if ("http://swapi.dev/api/species/1/" in character['species']):
        personaje_humano += 1
   elif ("http://swapi.dev/api/species/2/" in character['species']):
       personaje_droide += 1
       

print("Hay: ", personaje_droide, "personajes droides")
print("Hay: ", personaje_humano, "personajes humanos")

#! Listar todos los personajes que comienzan con C, L, A


# for character in sw_data:
#     if(character['name'][0] in ['C', 'L', 'A']):
#         print(character['name'])