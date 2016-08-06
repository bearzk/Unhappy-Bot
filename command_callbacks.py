from os import system
from datetime import timedelta

from config import Config
from telegram.ext.dispatcher import run_async

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
