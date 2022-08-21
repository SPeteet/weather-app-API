# Installed module 'requests' via terminal. Allows a request to the API
from dataclasses import dataclass
import requests 

API_KEY = "ac9f022136a7ba86ffdc8c5bb8106192"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = ''

while city != 'z':
    city = input("Enter a city name or 'z' to quit: ")

    if city =='z':
        print("Thank you for trying the Weather Fetcher application!")
        break

    # Creating url to send an API call. This code was provided by the API holder.
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url) # Creating get request

    if response.status_code == 200:
        api_data = response.json()
        clouds = api_data['weather'][0]['description']
        temperature_in_kelvin = api_data['main']['temp']
        temperature_in_celsius = round(temperature_in_kelvin - 273.15)
        temperature_in_fahrenheit = round(((temperature_in_kelvin - 273.15) * 9) / 5 + 32)
        humidity = api_data['main']['humidity']

        print(f'{city.title()} weather:')
        print(f'Temperature in Celsius: {temperature_in_celsius}\u00B0')
        print(f'Temperature in Fahrenheit: {temperature_in_fahrenheit}\u00B0')
        print(f'Weather Description: {clouds}')
        print(f'Humidity: {humidity}%')
    else:
        print("An error occurred or the city was not located, please try again.")
