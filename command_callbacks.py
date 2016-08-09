from os import system
from datetime import timedelta

from telegram.ext.dispatcher import run_async
import requests

from config import Config
from callback_decorators import authorized

@run_async
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a robot, please talk to me!")

@run_async
def whoami(bot, update):
    user = update.message.from_user
    text = "Your name is %s %s\n" % (user.first_name, user.last_name)
    text += "Your id is %s" % user.id
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

@run_async
@authorized
def stats(bot, update):
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))

    bot.sendMessage(chat_id=update.message.chat_id, text=uptime_string)

@run_async
def translate(bot, update):
    source = update.message.text.replace('/trans ', '').strip()
    if source:
        query = "https://glosbe.com/gapi/translate?from=deu&dest=eng&format=json&phrase=%s" % source
        res = requests.get(query)
        translations = res.json()['tuc']
        if translations:
            trans = [t['phrase']['text'] for t in translations if t.has_key('phrase')]
            message = "Translations found for word %s :\n" % source
            message += "\n".join(trans)
        else:
            message = "No translation found for word %s" % source
        bot.sendMessage(chat_id=update.message.chat_id, text=message)
