import logging
from config import Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from command_callbacks import start, whoami, stats, trans
from message_callbacks import echo

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def main():
    updater = Updater(token=Config['token'])

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    whoami_handler = CommandHandler('whoami', whoami)
    stats_handeler = CommandHandler('stats', stats)
    trans_handler = CommandHandler('trans', trans)

    echo_handler = MessageHandler([Filters.text], echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(whoami_handler)
    dispatcher.add_handler(stats_handeler)
    dispatcher.add_handler(trans_handler)

    dispatcher.add_handler(echo_handler)

    updater.start_polling(1)

    updater.idle()

if __name__ == '__main__':
    main()
