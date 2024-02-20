Тестовое задание: Python Разработчик
Примечание
Пишите код с комментариями.
Используйте ООП.
Учитывайте все возможные баги.
Готовый код сохранить на github и предоставить ссылку для проверки в ТГ  @Shamanim_vmeste. 
При отправке ответа, пожалуйста  - сообщите свои фамилию и имя в сообщении. Наш HR максимально быстро свяжется с тех лидом для проверки. Фидбэк будем стараться дать быстро - мы ценим время, которое вы потратили на работу - наш HR очень заинтересован, чтобы вашему заданию уделили внимание) 
Предполагаемое время выполнения тестового задания - 2 часа.
WebApp
Создать веб приложение используя Flask
При запуске приложения создается простая база данных SQLite, для управления списком пользователей(`users`) с полями(`id`, `username`, `balance`) с 5 пользователями и балансом от 5000 до 15000
Напишите Python-класс `User`, который представляет пользователя и взаимодействует с базой данных для добавления, обновления и удаления пользователей и обновления их балансов
Используя библиотеку `requests`, напишите функцию `fetch_weather(city)`, которая принимает на вход название города и возвращает текущую температуру в этом городе. Используйте любое открытое API для получения данных о погоде. Важно, вы можете использовать погрешность, температура меняется не чаще 10 минут
Написать route для обновления баланса пользователя, как в большую, так и в меньшую сторону на сумму равную температуре воздуха в выбранном городе, принимающего параметры userId, city.
Важным условием является то, что баланс пользователя не может быть отрицательным.
Изменение баланса должно производиться в реальном времени, без использования очередей и отложенных задач.
Тестирование
Мы фиксируем 5 рандомных городов
Отправляет запросы хаотично на протяжении 20 минут
В один рандомный момент отправим 1000 запросов в секунду
Система должна корректно и быстро обработать все запросы

Желаем успехов в выполнении!

Как запустить

pip install -r requirements.txt 
в строке   api_key = 'Ваш_api'  # Пожалуйста, замените YOUR_API_KEY на реальный ключ API
замените на реальный api ключ
Запустите приложение python main.py
Далее test.py
ab -n 1000 -c 100 http://127.0.0.1:5000/update_balance