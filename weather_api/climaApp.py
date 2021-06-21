from weather_API import clima_por_lat_lon
from weather_API import clima_por_ciudad
from weather_API import pronostico_por_lat_lon



# selec_1 = input("si quiere buscar el clima por ciudad, escriba 1 // si quiere buscar el clima por latitud y longitud escriba 2")
# selec_2 = input("si desea el clima actual, escriba actual // si desea el pronostico de los próximos días escriba futuro")

# if(selec_1 == 1 and selec_2 == 2):
    
ciudad = input("ingrese la ciudad para la búsqueda: ")
data = clima_por_ciudad(ciudad)

print(data)

lat = input("ingrese latitud: ")
lon = input("ingre la longitud: ")
data = pronostico_por_lat_lon(lat, lon)

print(data)

lat = input("ingrese latitud: ")
lon = input("ingre la longitud: ")
data = clima_por_lat_lon(lat, lon)

print(data)