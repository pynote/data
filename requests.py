import requests

# Coordinates for Tokyo
latitude = 35.6895
longitude = 139.6917

URL = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m"
)

response = requests.get(URL)
print("Status code:", response.status_code)

if response.status_code != 200:
    print("Error while calling the API")
    print("Response:", response.text)
else:
    data = response.json()
    current = data.get("current", {})

    temperature = current.get("temperature_2m")
    humidity = current.get("relative_humidity_2m")

    print("Current weather (Open-Meteo):")
    print(f"  Temperature: {temperature} °C")
    print(f"  Humidity: {humidity} %")
