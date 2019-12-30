import requests
import json

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
locale = {'city': '400010'}
data = requests.get(url, params = locale).json()

print(data['forecasts'][0]['date'])
print(data['forecasts'][0]['telop'])