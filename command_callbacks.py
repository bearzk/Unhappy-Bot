from os import system
from datetime import timedelta

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
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
def trans(bot, update):
    word = update.message.text.replace('/trans ', '').strip()
    if word:

        keyboard = [
            [
                InlineKeyboardButton("De->En", callback_data=" ".join([word, 'deu', 'eng'])),
                InlineKeyboardButton("En->De", callback_data=" ".join([word, 'eng', 'deu']))
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.sendMessage(chat_id=update.message.chat_id,
            text="Between which languages?", reply_markup=reply_markup)

@run_async
def trans_callback(bot, update):
    query = update.callback_query
    params = query.data.split(" ")
    message = _trans(*params)
    bot.editMessageText(
        text=message,
        chat_id=query.message.chat_id,
        message_id=query.message.message_id
    )

def _trans(word, origin='deu', dest='eng'):
    query = "https://glosbe.com/gapi/translate?from=%s&dest=%s&format=json&phrase=%s" % (origin, dest, word)
    res = requests.get(query)
    translations = res.json()['tuc']
    message = "No translation found for word %s" % word
    if translations:
        trans = [t['phrase']['text'] for t in translations[:10] if t.has_key('phrase')]
        message = "Translations found for word %s :\n" % word
        message += "\n".join(trans)
    return message

@run_async
def game(bot, update):
    text =
    """
    Ok let's play guess number!

    I have a number between 0 and 100 in my mind.
    You guess what it is, I can only tell you if you answer is larger or smaller.
    If you manage to guess it within 10 tries, you win!
    ready to play?
    """

    keyboard = [
        [
            InlineKeyboardButton("Yes", callback_data=True)
            InlineKeyboardButton("No", callback_data=False)
        ]
    ]

    reply_markup=InlineKeyboardMarkup(keyboard)

    bot.sendMessage(chat_id=update.message.chat_id
        text=text
        reply_markup=reply_markup
    )

@run_async
def game_callback(bot, update):
    data = update.callback_query.data
    bot
