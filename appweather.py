import requests

api_key = '457b5ee6554cbb2042657cd53efd3801'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"the weather in {user_input} is: {weather}")
print(f"the temperature in {user_input} is: {temp}F")


