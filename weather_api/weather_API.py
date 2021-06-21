import json
import requests

def obtener_clima(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
       dic = json.loads(req.text)
       return dic
    else:
        print('Error')

def pronostico_por_lat_lon(lat, lon):

    url_lat_lon = 'https://api.openweathermap.org/data/2.5/onecall?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    latitud = lat
    longitud = lon
    units = "metric"

    parametros = {"lat":latitud, "lon":longitud, "units": units, "appid":api_key}

    response = requests.get(url_lat_lon, params=parametros)

    data = json.loads(response.content)

    print("el pronóstico para la próxima hora es: ")   
    print('Temperatura:', str(data['hourly'][0]['temp']))
    print('Sensación térmica:', str(data['hourly'][0]['feels_like']))
    print('Humedad:', str(data['hourly'][0]['humidity']))

def clima_por_lat_lon(lat, lon):

    url_lat_lon = 'https://api.openweathermap.org/data/2.5/onecall?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    latitud = lat
    longitud = lon
    units = "metric"

    parametros = {"lat":latitud, "lon":longitud, "units": units, "appid":api_key}

    response = requests.get(url_lat_lon, params=parametros)

    data = json.loads(response.content)

    print("el clima actual es: ")   
    print('Temperatura:', data['current']['temp'])
    print('Sensación térmica:', data['current']['feels_like'])
    print('Humedad:', data['current']['humidity'])




def clima_por_ciudad(ciudad):
    url_ciudad = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    ciudad = ciudad
    unidades = "metric"

    parametros = {"q":ciudad, "units": unidades, "appid":api_key}

    response = requests.get(url_ciudad, params=parametros)

    data = json.loads(response.content)

    
    print('Latitud:', data['coord']['lat'])
    print('Longitud', data['coord']['lon'])
    print('Temperatura:', data['main']['temp'])
    print('Sensación térmica:', data['main']['feels_like'])
    print('Temperatura mínima:', data['main']['temp_min'])
    print('Temperatura máxima:', data['main']['temp_max'])
    print('Humedad:', data['main']['humidity'])
    
    

  
ciudad = input("ingrese la ciudad para la búsqueda: ")
data_clima_ciudad = clima_por_ciudad(ciudad)

print(data_clima_ciudad)

lat= input("ingrese latitud: ")
lon = input("ingrese la longitud: ")
data_lat_lon = clima_por_lat_lon(lat, lon)

print(data_lat_lon)
