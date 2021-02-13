from flask import Flask, json, jsonify
import requests
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getWeather():
    api_key = os.getenv("API_KEY")
    url = f'https://api.openweathermap.org/data/2.5/weather?q=los angeles&appid={api_key}&units=imperial'
    try:
        response = requests.get(url)
        print(f'Response: {response.text}')
        return jsonify(response.json())
    except Exception:
        return f"Could not process request", 404
