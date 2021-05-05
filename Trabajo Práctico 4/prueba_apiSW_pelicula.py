import json
import requests


#de esta manera anda OK
def get_peliculas(ruta):
   req = requests.get(ruta)
   # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
   if req.status_code == 200:
        dic = json.loads(req.text)
        return dic

result = get_peliculas("https://swapi.dev/api/films/1/")

print(result)

"""

#de esta manera no anda 
def get_peliculas(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if requests.status_code == 200:
        dic = json.loads(requests.text) 
        return dic 

result = get_peliculas("https://swapi.dev/api/films/1/")

print(result)
"""

