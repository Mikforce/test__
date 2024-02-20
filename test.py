# import requests
# import json
#
# # URL вашего Flask приложения
# url = 'http://127.0.0.1:5000/update_balance'
#
# # JSON данные для запроса, userId - идентификатор пользователя, city - название города
# data = {
#     'userId': 2,
#     'city': 'Moscow'
# }
#
# # Отправка POST запроса
# response = requests.post(url, json=data)
#
# # Вывод результата запроса
# print(response.text)
import requests
import json

url = 'http://127.0.0.1:5000/update_balance'
data = {
    'userId': 2,
    'city': 'Moscow'
}

for i in range(1000):
    response = requests.post(url, json=data)
    print(f"Запрос {i+1}: {response.text}")