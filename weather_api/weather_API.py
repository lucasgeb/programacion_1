import json
import requests

def obtener_clima(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
       dic = json.loads(req.text)
       return dic
    else:
        print('Error')

# url_lat_lon = 'https://api.openweathermap.org/data/2.5/onecall?'
# api_key = '6a19af64431d36030095df61d4e2abdd'
# latitude = input("ingrese Latitud ")
# longitude = input("ingrese Longitud ")
# units = "metric"

# parametros = {"lat":latitude, "lon":longitude, "units": units, "appid":api_key}

# response = requests.get(url_lat_lon, params=parametros)

 
# data = json.loads(response.content)
# data_sorted = sorted(data['current'].items())

# print(data_sorted)


# url_ciudad = 'https://api.openweathermap.org/data/2.5/weather?'
# api_key = '6a19af64431d36030095df61d4e2abdd'
# ciudad = input("ingrese la ciudad para la búsqueda: ")
# unidades = "metric"

# parametros = {"q":ciudad, "units": unidades, "appid":api_key}

# response = requests.get(url_ciudad, params=parametros)

 
# data = json.loads(response.content)
# data_sorted = sorted(data.items())

# print(data_sorted)

def clima_por_lat_lon(lat, lon):

    url_lat_lon = 'https://api.openweathermap.org/data/2.5/onecall?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    latitud = lat
    longitud = lon
    units = "metric"

    parametros = {"lat":latitud, "lon":longitud, "units": units, "appid":api_key}

    response = requests.get(url_lat_lon, params=parametros)

 
    data = json.loads(response.content)
    data_sorted = sorted(data['current'].items())

    return(data_sorted)


def clima_por_ciudad(ciudad):
    url_ciudad = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    ciudad = ciudad
    unidades = "metric"

    parametros = {"q":ciudad, "units": unidades, "appid":api_key}

    response = requests.get(url_ciudad, params=parametros)

 
    data = json.loads(response.content)
    data_sorted = sorted(data.items())

    return(data_sorted)