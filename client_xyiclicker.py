""" Короче сделано крутыми челами куплено у крутых челов @ftgmodules_bot """
from time import sleep
from pyrogram import Client

API_HASH = 'ApiHash'
API_ID = 'ApiId'

app = Client("clicker", API_ID, API_HASH)

timeout = 1 # Тайм-Аут = Задержка. Во избежания анти-флуда оставьте единицу.


@app.on_message()
def huyaru(client, message):
    if message.chat.id == 1198158349:
        if message.media:
            print('WARN! picture spotted')
            return
        sleep(timeout)
        for j in message.reply_markup['keyboard']:
            first = ([w[0] for w in j[0]])
            second = [w[0] for w in j[1]]
            third = [w[0] for w in j[2]]

            for b in [first, second, third]:
                if '⭕' in b:
                    text = ''.join(b)
                    message.reply_text(text)


app.run()
