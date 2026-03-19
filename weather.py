import requests
url = "https://api.openweathermap.org/data/2.5/weather"

while True:
    city = input("please input a city: ")

    params = {
        "q" : city,
        "appid" : "cc5bd20949827335b8ae8b38710f0881",
        "units" : "imperial"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data["cod"] != 200:
            print(f"'{city}' not found. please check the spelling.")
            print("-------------------------------------------------------")
            
        else: 
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
            break

    except requests.exceptions.RequestsException:
        print("network error. check your connection and try again.")
        print("----------------------------------------------------")