
# importing geopy library
from geopy.geocoders import Nominatim
import requests
import os
import time
import schedule
import ctypes
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
userLocation = input('enter town and state: ')
getLoc = loc.geocode(userLocation)
lat = str(round(getLoc.latitude,4))
lon = str(round(getLoc.longitude, 4))
x = requests.get('https://api.weather.gov/points/'+lat+','+lon+'')
y = x.json()
z = y['properties']['forecast']
xyz = requests.get(z)
forecast = xyz.json()

def timedAlert():
    print(forecast['properties']['periods'][0]['detailedForecast'])
    print(getLoc.address)
    ctypes.windll.user32.MessageBoxW(0,forecast['properties']['periods'][0]['detailedForecast'], "Weather", 0 )
schedule.every().day.at("08:24").do(timedAlert())

def callApi():
    print(forecast['properties']['periods'][0]['detailedForecast'])
    print(getLoc.address)
    ctypes.windll.user32.MessageBoxW(0,forecast['properties']['periods'][0]['detailedForecast'], "Weather", 0 )

while True:
    schedule.run_pending()
    
    time.sleep(1)