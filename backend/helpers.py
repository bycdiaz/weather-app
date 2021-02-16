import os


def set_key():
    return os.getenv("API_KEY")


def set_url(city):
    return f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={set_key()}&units=imperial'
