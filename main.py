from flask import Flask, request
from flask_caching import Cache
import sqlite3
import requests

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

class User:
    def __init__(self, id, username, balance):
        self.id = id
        self.username = username
        self.balance = balance

    def update_balance(self, new_balance):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, self.id))
        conn.commit()
        conn.close()

def fetch_weather(city):
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        return temperature_celsius
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def get_user_balance(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

@app.route('/update_balance', methods=['POST'])
@cache.memoize(timeout=60)  # Cache the result of this function for 60 seconds
def update_balance():
    user_id = request.json.get('userId')
    city = request.json.get('city')

    temperature = fetch_weather(city)

    user_balance = get_user_balance(user_id)

    new_balance = user_balance + temperature if user_balance + temperature >= 0 else 0
    user = User(user_id, 'username', user_balance)
    user.update_balance(new_balance)

    return 'Balance successfully updated'

if __name__ == '__main__':
    app.run()