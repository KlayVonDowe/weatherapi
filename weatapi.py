
# importing geopy library
from geopy.geocoders import Nominatim
import requests
import os
 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
userLocation = input('enter town and state: ')
getLoc = loc.geocode(userLocation)
lat = str(round(getLoc.latitude,4))
lon = str(round(getLoc.longitude, 4))
# printing address
print(getLoc.address)
 
# printing latitude and longitude

x = requests.get('https://api.weather.gov/points/'+lat+','+lon+'')
y = x.json()
z = y['properties']['forecast']
xyz = requests.get(z)
forecast = xyz.json()
print(forecast['properties']['periods'][0]['detailedForecast'])