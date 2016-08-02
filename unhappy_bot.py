import logging
from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=Config['token'])

dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a robot, please talk to me!")

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler([Filters.text], echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

updater.idle()
