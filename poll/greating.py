import json
import requests
import os
import time
TOKEN = os.environ['telegram_token']
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_target_name(last_message):
    if 'username' in last_message["message"]["from"]:
        target_name = last_message["message"]["from"]["username"]
    else:
        target_name = last_message["message"]["from"]["first_name"]
    return(target_name)

def say_hello(target_name, chat_id):
    url = f"{URL}sendMessage?text=Hello {target_name}&chat_id={chat_id}"
    get_url(url)

def send_message(chat_id):
    text = 'How are you?'
    url = f"{URL}sendMessage?text={text} &chat_id={chat_id}"
    get_url(url)


def main():
    history = get_updates()
    num_updates = len(history["result"])
    last_message_num = num_updates - 1
    last_message = history["result"][last_message_num]
    chat_id = last_message["message"]["chat"]["id"]
    target_name = get_target_name(last_message)
    last_message_text = last_message["message"]["text"]
    
    if 'Hello' or 'Привет' or 'алоха' in last_message_text:
        say_hello(target_name, chat_id)
    else:
        send_message(chat_id)

if __name__ == '__main__':
    main()