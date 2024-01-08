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
    retrieve_weather_data()
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

@app.route('/weather')
def get_weather():
    db = connect_database()
    collection = db["weather"]

    past_24_hours = datetime.now() - timedelta(hours=24)
    weather_data_list = list(collection.find({"timestamp": {"$gte": past_24_hours}}))

    if len(weather_data_list) > 0:
        statistics = calculate_statistics(weather_data_list)
        return jsonify(statistics)
    else:
        return "No weather data available."

def start_http():
    global listen_port
    if listen_port is None:
        listen_port = "3333"
    @app.route('/')
    def index():
        return 'Hello World'
    app.run(host='0.0.0.0', port=int(listen_port))
# ... (remaining code is unchanged)

if __name__ == "__main__":
    main()


