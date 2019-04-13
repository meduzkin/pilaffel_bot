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

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1

    username = updates["result"][last_update]["message"]["chat"]["username"]
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    first_name = updates["result"][last_update]["message"]["chat"]["first_name"]
    return (text, chat_id, first_name)
    # username,
    # return (username, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def write_first_name(first_name, chat_id):
    # url = URL + "sendMessage?text={}&chat_id={}".format('Hello '+ first_name, chat_id)
    url = f"{URL}sendMessage?text=Hello {first_name}&chat_id={chat_id}"
    get_url(url)


def main():
    last_textchat = (None, None)
    while True:
        text, chat, first_name  = get_last_chat_id_and_text(get_updates())
        #username,
        if (text, chat, first_name) != last_textchat:
            #username,
            write_first_name(first_name, chat)
            # send_message(text, chat)
            last_textchat = (first_name, chat)
        time.sleep(0.5)

if __name__ == '__main__':
    main()