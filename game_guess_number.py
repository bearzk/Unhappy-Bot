from random import random
from math import ceil

class GuessNumber(object):

    def __init__(self, bot, update, range=100, limit=10):
        self.bot = bot
        self.update = update
        self.guesses = 0
        self.number = int(ceil(random() * range))
        self.limit = limit

    def guess(self, number):
        self.guesses += 1
        if self.guesses > self.guess_limit:
            message = "You didn't manage within %d times :(" % self.guess_limit
            self._reply(message)
            return

        if number == self.number and not self.guesses > self.guess_limit:
            self.bot.sendMessage(
                chat_id=self.update.message.chat_id
                text="Wow, you finished the game with %d guesses" % self.guesses
            )
            return
        message = "Smaller!" if number > self.number else "Larger!"
        self._reply(message)

    def _reply(self, message):
        self.bot.sendMessage(
            chat_id=self.update.message.chat_id,
            text=message
        )
