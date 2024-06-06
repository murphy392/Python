#trial ends on Jun 20 2024

import requests

city = 'Orland'

url = 'http://api.weatherapi.com/v1/current.json?key=511b05c497704381b13172459240606&q='+ city +'&aqi=no'

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, "is", description, 'and', temp, 'degrees')
