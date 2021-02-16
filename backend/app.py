from flask import Flask, jsonify
import sqlite3
import requests

from helpers import set_url

app = Flask(__name__)


def create_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute(
        'CREATE TABLE IF NOT EXISTS weather (city TEXT UNIQUE ON CONFLICT REPLACE, feels_like REAL, description TEXT, icon TEXT)')
    print("Table created successfully")

    conn.close()


def getWeather():
    url = set_url('Dallas')
    try:
        response = requests.get(url)
        json_response = response.json()
        return json_response
    except Exception:
        return f"Could not process request", 404


@app.route('/', methods=['GET'])
def send_to_db():
    create_db()
    api_response = getWeather()
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
