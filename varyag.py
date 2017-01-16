'''
Бот по запросу отправляет последний выложенный воркаут в зале Varyag
'''
# coding: utf-8

import urllib.request
import simplejson as json
import sys
import time
import telepot


def handle(msg):
    chat_id = msg["chat"]["id"]
    command = msg["text"]
    print("Got command: {}".format(command))

    #Обработка команды "/wod": на запрос к API vk.com получаем ответ в JSON
    if command == "/wod":
        req_cf = urllib.request.urlopen("https://api.vk.com/method/wall.get?domain=varyag_cf").read()
        dt = json.loads(req_cf)

        #По тегу "#WOD" находит первый пост с воркаутом
        for post in dt["response"]:
            try:
                if post["text"].find("#WOD") != -1:
                    wod = post["text"].replace("<br>", "\n")
                    break
            except:
                continue
        bot.sendMessage(chat_id, wod)

    #Обработка команды "/help"
    elif command == "/help":
        bot.sendMessage(chat_id, 'Введите "/wod", чтобы получить последний выложенный воркаут')

bot = telepot.Bot(sys.argv[1])
bot.message_loop(handle)
print ("Listening...")

while 1:
    time.sleep(10)
