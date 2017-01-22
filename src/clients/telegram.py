import os
import logging
import clients
import textwrap

from persist import JsonObject
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from webpreview import web_preview

class TelegramBot(object):

    def __init__(self, token, reddit):
        self.chats = JsonObject('chats.json')
        self.updater = Updater(token)
        self.reddit = reddit
        self.updater.dispatcher.add_handler(MessageHandler(Filters.status_update, self._status))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.entity('url'), self._url))

        for c in 'start stop help post'.split():
            self.updater.dispatcher.add_handler(CommandHandler(c, getattr(self, '_' + c)))

    def _start(self, bot, update):
        update.message.reply_text(textwrap.dedent('''
            Hello. I will send the links on this chat to Reddit.
            Send /help for more information.
            ''').strip())

    def _help(self, bot, update):
        text = textwrap.dedent('''
        This bot sends all links message in this chat to a subreddit you choose.

        Commands:
        /start      : Show the welcome message.
        /help       : This message.
        /post <sub> : Set the subreddit which to post links to.
        /post       : Show which subreddit it is posting to.
        /stop       : Stop sending links to reddit.
        ''').strip()
        update.message.reply_text(text)

    def _post(self, bot, update):
        if not self.chats.data:
            self.chats.load()

        m = update.message
        params = m.text.split()
        if len(params) < 2:
            subreddit = self.chats[update.message.chat.id]
            if subreddit:
                text = 'This bot is sending links to /r/' + subreddit
            else:
                text = 'This bot was not configured yet.'
            text += textwrap.dedent('''

            Please inform the subreddit alongside the command to send the links
            posted on this chat to {} subreddit.
            e.g: /post pics
            '''.format('another' if subreddit else 'a'))
            m.reply_text(text)
            return

        subreddit = params[1]
        if not self.reddit.exists(subreddit):
            m.reply_text('The subreddit "{}" doesn\'t exist!'.format(subreddit))
            return

        self.chats[m.chat.id] = subreddit
        self.chats.save()
        m.reply_text('All links from "{}" will be posted to {}'.format(
                        m.chat.title or m.chat.username, subreddit))


    def _url(self, bot, update):
        url = update.message.text
        title, description, image = web_preview(url)
        subreddit = self.chats[update.message.chat.id]
        self.reddit.submit(subreddit, title, url)

    def _stop(self, bot, update):
        m = update.message
        m.reply_text('This bot will no longer post links to reddit.')
        del self.chats[m.chat.id]

    def _status(self, bot, update):
        m = update.message
        if hasattr(m, 'new_chat_member') and m.new_chat_member.id == bot.id:
                self._start(bot, update)
        if hasattr(m, 'left_chat_member') and m.new_chat_member.id == bot.id:
                self._finish(bot, update)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()
