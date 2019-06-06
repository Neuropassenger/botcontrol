# -*- coding: utf-8 -*-

import config
import requests
import pprint

api_url = "https://api.telegram.org/bot{}/".format(config.TOKEN)

# Метод для получения последних обновлений за 24 часа
def get_updates(offset=None, timeout=100):
    params = {'timeout': timeout, 'offset': offset}  # Параметры API метода getUpdates
    response = requests.get(api_url + 'getUpdates', params)
    result_json = response.json()
    pprint.pprint(result_json)

    return result_json

# Метод отправки сообщения через консоль
def send_message():
    chat_id = int(input('Введите ID чата -> '))
    text = str(input('Введите ваше сообщение -> '))
    reply_message_id = input('Введите ID сообщения для ответа (пустая строка - ответ не нужен) ->')

    global additional_params
    additional_params = {}
    # Добавляем reply_to_message_id в список параметров, если нужно ответить на  сообщение
    if reply_message_id != "":
        additional_params = {'reply_to_message_id': int(reply_message_id)}

    params = {'chat_id': chat_id, 'text': text}     # Параметры API метода sendMessage
    # Конкатенация словарей параметров
    params = {**params, **additional_params}
    # Выполняем запрос к API
    response = requests.get(api_url + 'sendMessage', params)
    result_json = response.json()
    pprint.pprint(result_json)

    return result_json

while True:
    get_updates()
    send_message()
