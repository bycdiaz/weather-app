from flask import Flask
app = Flask(__name__)


@app.route('/')
def getWeather():
    return 'Hello, World!'
