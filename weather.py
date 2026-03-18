import requests
url = "https://api.openweathermap.org/data/2.5/weather"

city = input("please input a city: ")

params = {
    "q" : city,
    "appid" : "cc5bd20949827335b8ae8b38710f0881",
    "units" : "imperial"
}

response = requests.get(url, params=params)
data = response.json()
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