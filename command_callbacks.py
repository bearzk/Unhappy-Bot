from config import Config
from telegram.ext.dispatcher import run_async

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
def scream(bot, update):
    user = update.message.from_user
    message = "You are not allowed here"
    if user.id in Config['authorized']:
        message = "You should be happy"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
