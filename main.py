from flask import Flask, request
import sqlite3
import requests

app = Flask(__name__)

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
    api_key = '661ebedb04a615ee09c54592b4b2a55c'  # Пожалуйста, замените YOUR_API_KEY на реальный ключ API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    return temperature_celsius

def get_user_balance(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = cursor.fetchone()[0]  # Получаем первое значение столбца
    conn.close()
    return balance

@app.route('/update_balance', methods=['POST'])
def update_balance():
    user_id = request.json.get('userId')
    city = request.json.get('city')

    temperature = fetch_weather(city)

    user_balance = get_user_balance(user_id)  # Получаем текущий баланс пользователя из базы данных

    new_balance = user_balance + temperature if user_balance + temperature >= 0 else 0
    user = User(user_id, 'username', user_balance)
    user.update_balance(new_balance)

    return 'Баланс успешно обновлен'

if __name__ == '__main__':
    app.run()