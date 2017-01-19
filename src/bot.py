import os
import logging
import clients

from clients.abc import Chatter, Publisher
from clients.telegram import TelegramBot
from clients.reddit import RedditBot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

REDDIT = {
    'client_id'     : os.environ['TELEGRAM_REDDIT_ID'],
    'client_secret' : os.environ['TELEGRAM_REDDIT_SECRET'],
    'username'      : os.environ['TELEGRAM_REDDIT_USERNAME'],
    'password'      : os.environ['TELEGRAM_REDDIT_PASSWORD'],
}
clients.register(Publisher, RedditBot(**REDDIT))

TOKEN = os.environ['TELEGRAM_REDDIT_TOKEN']
bot = TelegramBot(TOKEN)
clients.register(Chatter, bot)

print('Listening ...')
bot.run()
