from telegram.ext.dispatcher import run_async
@run_async
def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
