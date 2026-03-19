import requests
import json
import os
from datetime import datetime

url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    
    params = {
        "q" : city,
        "appid" : "cc5bd20949827335b8ae8b38710f0881",
        "units" : "imperial"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["cod"] != 200:
        return None
    return data

def display_weather(city, data):

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("---------------------------")
    print(f"  Weather for {city.title()}")
    print("---------------------------")
    print(f"  Temperature : {temp}°F")
    print(f"  Conditions  : {description.title()}")
    print(f"  Humidity    : {humidity}%")
    print("---------------------------")

def save_result(city, data):
    tempSave = data["main"]["temp"]
    descriptionSave = data["weather"][0]["description"]
    humiditySave = data["main"]["humidity"]
    timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "city" : city,
        "temperature" : tempSave,
        "conditions" : descriptionSave,
        "humidity" : humiditySave,
        "timestamp" : timeStamp
    }

    if os.path.exists("weather_log.json"):
        with open("weather_log.json", "r") as f:
            log = json.load(f)
    else:
        log = []

    log.append(entry)

    with open("weather_log.json", "w") as f:
        json.dump(log, f, indent=4)


while True:
    try:
        city = input("please input a city: ")
        data = get_weather(city)
        
        if data is None:
            print(f"'{city}' not ofund. please check your spelling and try again.")
            print("------------------------------------------------------------------------")
        else: 
            display_weather(city, data)
            save_result(city, data)
            break

    except requests.exceptions.RequestException:
        print("network error. check your connection and try again.")
        print("----------------------------------------------------")