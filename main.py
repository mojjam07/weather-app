import requests

API_KEY = "70305c1a89bcf968fe7f89f62bb81d56"
CITY = "Lagos"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

print(f"City: {data['name']}")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Weather: {data['weather'][0]['description']}")