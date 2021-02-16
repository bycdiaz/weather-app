from flask import Flask, jsonify, request
from flask_cors import CORS

import sqlite3
import requests

from helpers import set_url

app = Flask(__name__)
CORS(app)


def create_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute(
        'CREATE TABLE IF NOT EXISTS weather (city TEXT UNIQUE ON CONFLICT REPLACE, feels_like REAL, description TEXT, icon TEXT)')
    conn.execute(
        'CREATE TABLE IF NOT EXISTS locationinfo (city TEXT UNIQUE ON CONFLICT REPLACE, notes TEXT)')
    print("Table created successfully")

    conn.close()


create_db()


def getWeather(city_name):
    url = set_url(city_name)
    try:
        response = requests.get(url)
        json_response = response.json()
        return json_response
    except Exception:
        return f"Could not process request", 404


def save_weather_to_db(city_name):

    api_response = getWeather(city_name)
    name, main, weather = [api_response[x]
                           for x in ('name', 'main', 'weather')]
    city = name
    feels_like = main['feels_like']
    description = weather[0]['description']
    icon = weather[0]['icon']

    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO weather (city, feels_like, description, icon) VALUES (?,?,?,?)",
                    (city, feels_like, description, icon))
        con.commit()
        msg = "Records added!"
        print(msg)
    return api_response


def save_user_input_to_db(city, notes):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO locationinfo (city, notes) VALUES (?,?)",
                    (city, notes))
        con.commit()
        msg = "Records added!"
        print(msg)


@app.route('/', methods=['GET'])
@app.route('/forminput', methods=['POST'])
def get_form_info():
    form_input = request.json

    city, notes = [form_input[x]
                   for x in ('cityName', 'notes')]
    save_weather_to_db(city)
    save_user_input_to_db(city, notes)
    return request.json
