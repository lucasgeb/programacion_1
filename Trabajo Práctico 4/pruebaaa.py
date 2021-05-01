
def busqueda(data, buscado):
    pos = -1
    for index, personaje in enumerate(data):
        if(personaje["name"] == buscado):
            pos = index
    return pos

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
for character in sw_data:
    if(character["mass"].isdecimal()):
        if(int(character["mass"]) >= 100):
            print(character["name"], character["mass"])

#! Mostrar todos los personajes del planeta natal Tatooine y Coruscant

