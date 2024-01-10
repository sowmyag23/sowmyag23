from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    user_input = request.args.get('city')

    if not user_input:
        return jsonify({'error': 'City parameter is required'}), 400

    api_key = '30d4741c779ba94c470ca1f63045390a'
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json().get('cod') == '404':
        return jsonify({'error': 'City not found'}), 404
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])

        return jsonify({
            'city': user_input,
            'weather': weather,
            'temperature': temp
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

