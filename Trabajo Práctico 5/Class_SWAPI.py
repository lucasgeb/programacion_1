
#! IMPORTO DATA DE API
import json
import requests
from random import randint

def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic

#! IMPORTO PERSONAJES
def get_all_sw_characters():

    sw_data = []

    data = get_docs("https://swapi.dev/api/people/")

    while(data["next"] is not None):
        for personaje in data["results"]:
            sw_data.append(personaje) #print(doc["name"], doc["url"][28:-1])
        data = get_docs(data["next"])
    
    return sw_data

sw_data = get_all_sw_characters()


#! IMPORTO PERSONAJES POR ID
def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data

#! IMPORTO PLANETA POR ID
def get_planet_by_id(id):
    data = get_docs("https://swapi.dev/api/planets/"+str(id))
    return data


#! DEFINO LA CLASE PERSONAJE
class Personaje(object):
    def __init__(self,name, gender, hair_color, height, homeworld, mass, species=None, starships=None):
        self.__name = name
        self.__gender = gender
        self.__hair_color = hair_color
        self.__height = height
        self.__homeworld = homeworld
        self.__mass = mass
        self.__species = species
        self.__starships = starships

    @property
    def starships(self):
        return self.__starships
    
    @starships.setter
    def starships(self, starships):
        """Agregar manualmente nave si fué usada."""
        if(type(starships) is str):
            self.__starships = starships
        else:
            print('Escribí el nombre de la nave')

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        """Agregar manualmente la especie."""
        if(type(species) is str):
            self.__species = species
        else:
            print('Escribí la especie de este personaje ')

    @property
    def homeworld(self):
        return self.__homeworld
    
    def mostrar_datos(self):
        """Muestra los datos de cada planeta."""
        print(self.__name, self.__gender, self.__hair_color, self.__height, self.__mass, self.__species, self.__starships)
    

#! DEFINO LA CLASE PLANETA
class Planeta(object):
    def __init__(self, climate, diameter, name=None, orbital_period=None, rotation_period=None):
        self.__climate = climate
        self.__diameter = diameter
        self.__name = name
        self.__orbital_period = orbital_period
        self.__rotation_period = rotation_period
        

    
    def mostrar_datos(self):
        """Muestra los datos de cada persona."""
        print(self.__climate, self.__diameter, self.__name, self.__orbital_period, self.__rotation_period)

#! DEFINO LA CLASE ESPECIE
class Especie(object):
    def __init__(self, name, languaje, classification):
        self.__name = name
        self.__languaje = languaje
        self.__classification = classification
    def species_info(self):
        print(self.__name, self.__languaje, self.__classification)




pers1 = get_charter_by_id(2)
hom1 = get_planet_by_id(2)

especie_api = get_docs(pers1['species']) 

especie1 = Especie(especie_api['name'], especie_api['languaje'], especie_api['classification'])
planeta1 = Planeta(hom1['climate'], hom1['diameter'], hom1['name'], hom1['orbital_period'], hom1['rotation_period'])
personaje1 = Personaje(pers1['name'], pers1['gender'], pers1['hair_color'], pers1['height'], planeta1 , pers1['mass'], especie1, pers1['starships'])

#!AGREGO NAVE/ESPECIE SI NO ESTÁ
# personaje1.starships =
# personaje1.species =



#!MUESTRO LA INFO
personaje1.mostrar_datos()
personaje1.homeworld.mostrar_datos()


