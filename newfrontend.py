from flask import Flask, jsonify
from os import environ
from pymongo import MongoClient
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
listen_port = environ.get("HTTP_PORT")
db_name = environ.get("DB_NAME")
update_interval = int(environ.get("UPDATE_INTERVAL", 3600))
weather_location = environ.get("WEATHER_LOCATION")

def main():
    weatherdb = connect_database()
    print(f"Database: {weatherdb.name}")
    start_http()

def connect_database():
    if db_name is None:
        print("Must set DB_NAME in environment")
        exit(1)
    client = MongoClient("mongodb", 27017)
    print(client.server_info())
    return client[db_name]

def retrieve_weather_data():
    api_key = "7050ff93230770172103ab380dbcc811"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={weather_location}&appid={api_key}"

    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        print("Weather Data Retrieved Successfully:", weather_data)  # Add this line for debugging
        return weather_data
    else:
        print("Error retrieving weather data")
        return None

# ... (remaining code is unchanged)

if __name__ == "__main__":
    main()


