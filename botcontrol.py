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
    reply_message_id = input('Введите ID сообщения для ответа (пустая строка - ответ не нужен) -> ')

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

# Метод отправки голосового сообщения
def send_voice():
    chat_id = int(input('Введите ID чата -> '))
    voice_name = str(input('Введите название файла в папке res (без расширения) -> '))
    reply_message_id = input('Введите ID сообщения для ответа (пустая строка - ответ не нужен) -> ')

    params = {'chat_id': chat_id}

    # Добавляем reply_to_message_id в список параметров, если нужно ответить на  сообщение
    if reply_message_id != "":
        params['reply_to_message_id'] = int(reply_message_id)

    #for file in os.listdir('res/'):
        #if file.split('.')[-1] == 'ogg':
    voice = open('res/' + voice_name + '.ogg', 'rb')
    files = {'voice': voice}
    print(params)

    # Выполняем запрос к API
    response = requests.post(api_url + 'sendVoice', params, files=files)
    print(response)
    result_json = response.json()
    pprint.pprint(result_json)

    return result_json


# Метод отправки фото
def send_photo():
    #chat_id = int(input('Введите ID чата -> '))
    chat_id = 59887340
    file_name = str(input('Введите название файла в папке res (с расширением) -> '))
    reply_message_id = input('Введите ID сообщения для ответа (пустая строка - ответ не нужен) -> ')

    params = {'chat_id': chat_id}

    # Добавляем reply_to_message_id в список параметров, если нужно ответить на  сообщение
    if reply_message_id != "":
        params['reply_to_message_id'] = int(reply_message_id)

    file = open('res/' + file_name, 'rb')
    files = {'photo': file}
    print(params)

    # Выполняем запрос к API
    response = requests.post(api_url + 'sendPhoto', params, files=files)
    print(response)
    result_json = response.json()
    #pprint.pprint(result_json)

    return result_json


while True:
    get_updates()
    #send_message()
    send_voice()
