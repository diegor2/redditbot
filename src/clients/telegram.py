import os
import logging
import clients

from clients.abc import Chatter
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class TelegramBot(Chatter):
    def __init__(self, token):
        self.updater = Updater(token)
        self.updater.dispatcher.add_handler(MessageHandler(Filters.status_update, self._status))
        self.updater.dispatcher.add_handler(CommandHandler('hello', self._hello))

    def _hello(self, bot, update):
        update.message.reply_text(
            'Hello {}'.format(update.message.chat.type))

    def _status(self, bot, update):
        m = update.message
        if hasattr(m, 'new_chat_member') and m.new_chat_member.id == bot.id:
                print('invited to ' +  m.chat.title)
        if hasattr(m, 'left_chat_member') and m.new_chat_member.id == bot.id:
                print('kicked from ' +  m.chat.title)

    def ask_topic(self):
        pass

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
