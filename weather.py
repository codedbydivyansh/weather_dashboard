import requests
import os
import json
from dotenv import load_dotenv

HISTORY_FILE = "weather_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(entry):
    history = load_history()
    history = [h for h in history if h["city"] != entry["city"]]
    history.insert(0, entry)
    history = history[:5]
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

load_dotenv()

API_Key = os.getenv("OPENWEATHER_API_KEY")

history = load_history()

if history:
    print(f"Last searched city: {history[0]['city']}")
    
city = input("Enter city name : ")

if city.lower() == "history":
    history = load_history()

    if not history:
        print("No search history found.")
    else:
        print("\nLast 5 Searches:\n")

        for entry in history:
            print(
                f"{entry['city']} | "
                f"{entry['temp']}°C | "
                f"{entry['humidity']}% Humidity | "
                f"{entry['condition']} | "
                f"AQI {entry['aqi']}"
            )

    exit()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code != 200:
    print("Invalid city name.")
    exit()

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

entry = {
    "city": city,
    "temp": temp,
    "humidity": humidity,
    "condition": condition,
    "aqi": aqi
}
save_history(entry)