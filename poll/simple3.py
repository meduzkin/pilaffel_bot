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

def get_last_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    last_text = updates["result"][last_update]["message"]["text"]
    return (last_text)

def get_target_name(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    username = updates["result"][last_update]["message"]["chat"]["username"]
    first_name = updates["result"][last_update]["message"]["chat"]["first_name"]
    if first_name in last_update:
        target_name = username
    else:
        target_name = first_name
    # return (username)
    # return (first_name)
    return(target_name)

def get_chat_id(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return(chat_id)

def send_message(last_message):
    chat_id = last_message['chat_id']
    text = 'How are you?'
    url = f"{URL}sendMessage?text={text} &chat_id={chat_id}"
    get_url(url)

def say_hello_to(last_message):
    chat_id = last_message['chat_id']
    username = updates["result"][last_update]["message"]["chat"]["username"]
    first_name = updates["result"][last_update]["message"]["chat"]["first_name"]
    if 'username' in last_message['message']['chat']:
        target_name = username
    else:
        target_name = first_name
    url = f"{URL}sendMessage?text=Hello {target_name}&chat_id={chat_id}"
    get_url(url)

def main():
    while True:
        updates = get_updates()
        last_message = get_last_text(updates)
        target_name = get_target_name(updates)
        chat_id = get_chat_id(updates)
        # if 'Hello' in last_message:
        #     say_hello_to(taget_name)
        # else:
        #     send_message(updates)
        
        print(last_message)
        print(target_name)
        

if __name__ == '__main__':
    main()