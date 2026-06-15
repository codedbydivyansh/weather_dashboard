import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_Key = os.getenv("OPENWEATHER_API_KEY")
city = input("Enter city name :")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"

response = requests.get(url)
data = response.json()

temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
condition = data["weather"][0]["description"]

print(f"Weather in {city}")
print(f"Temperature  : {temp}°C (Feels like {feels_like}°C)")
print(f"Humidity     : {humidity}%")
print(f"Wind Speed   : {wind_speed} km/h")
print(f"Condition    : {condition}")