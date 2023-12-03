import requests
import weatherHandler

api_key = '8d7acff79461a9e1c5a997c3cf5c1384'

city = 'Grand Rapids'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

def checkWeather():
    if response.status_code == 200:
        data = response.json()
        desc = data['weather'][0]['description']
        print(f'Description: {desc}')
        if 'rain' in desc:
            weatherHandler.setWeather('rainy')
        elif 'snow' in desc:
            weatherHandler.setWeather('snowy')
        elif 'cloud' in desc:
            weatherHandler.setWeather('cloudy')
        elif 'sun' in desc:
            weatherHandler.setWeather('sunny')
        else:
            weatherHandler.setWeather('clear')
    else:
        print('Error fetching weather data')

## this code is an adaptation from the tutorial on website:
## https://medium.com/@rekalantar/how-to-build-a-simple-
## weather-app-in-python-with-openweathermap-api-447a2dd27898