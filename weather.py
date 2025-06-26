import requests

def get_weather(city):
    API_KEY = 'Paste your OpenWeatherMap API key here'

    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f'Weather in {city}: {temp}°C, {desc.capitalize()}')
    else:
        print('City not found or API error.')

city_input = input('Enter city name: ')
get_weather(city_input)