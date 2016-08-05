import logging
from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from command_callbacks import start, whoami, scream
from message_callbacks import echo

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=Config['token'])

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
whoami_handler = CommandHandler('whoami', whoami)
scream_handeler = CommandHandler('scream', scream)

echo_handler = MessageHandler([Filters.text], echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(whoami_handler)
dispatcher.add_handler(scream_handeler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

updater.idle()
