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

lat = data["coord"]["lat"]
lon = data["coord"]["lon"]

aqi_url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_Key}"

aqi_response = requests.get(aqi_url)
aqi_data = aqi_response.json()

aqi = aqi_data["list"][0]["main"]["aqi"]

aqi_levels = {
    1: "Good",
    2: "Fair", 
    3: "Moderate",
    4: "Poor",
    5: "Very Poor"
}

print(f"Air Quality  : {aqi} — {aqi_levels[aqi]}")

aqi_advisory = {
    1: "Air quality is satisfactory.",
    2: "Acceptable air quality.",
    3: "Sensitive individuals should reduce outdoor activity.",
    4: "Everyone may experience health effects.",
    5: "Avoid outdoor activity."
}

print(f"Advisory     : {aqi_advisory[aqi]}")