##API portion by Hannah Shaw
import requests

api_key = '8d7acff79461a9e1c5a997c3cf5c1384'

city = 'Grand Rapids'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    desc = data['weather'][0]['description']
    print(f'Description: {desc}')
    if 'rain' in desc:
        set_background('rain')
    elif 'snow' in desc:
        set_background('snow')
    elif 'cloud' in desc:
        set_background('cloud')
    elif 'tornado' or 'high wind' in desc:
        set_backgroud('wind')
    elif 'sun' in desc:
        set_backgrou('sun')
    else:
        set_background('default')
else:
    print('Error fetching weather data')
## this code is an adaptation from the tutorial on website:
## https://medium.com/@rekalantar/how-to-build-a-simple-
##weather-app-in-python-with-openweathermap-api-447a2dd27898
