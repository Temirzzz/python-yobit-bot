import requests
import misc
import json
from yobit import get_btc
from time import sleep

token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0 


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    # print(r.json())
    return r.json()

def get_message():
    data = get_updates()

    current_update_id = data['result'][-1]['update_id']    

    global last_update_id # указываем что будем использовать глобальную переменную

    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = data['result'][-1]['message']['chat']['id']
        message_text = data['result'][-1]['message']['text'] 

        message =  {'chat_id' : chat_id, 'text' : message_text}
        return message
    else:
        return None

def send_message(chat_id, text='Сейчас, секундочку...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text) # format() метод подставляет в фигурные скобки переменные chat_id и text
    print(url)
    requests.get(url)


def main():
    #data = get_updates()   

    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue

        sleep(2)



if __name__ == '__main__':
    main()