from flask import Flask, json, jsonify
import requests

from helpers import set_url

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getWeather():
    url = set_url()
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception:
        return f"Could not process request", 404
