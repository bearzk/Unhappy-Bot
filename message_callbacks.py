def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)
