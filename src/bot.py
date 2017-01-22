
import logging

from clients.telegram import TelegramBot
from clients.reddit import RedditBot

from persist import Config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

config = Config()
tokens = config['clients']

bot = TelegramBot(**tokens['telegram'], reddit = RedditBot(**tokens['reddit']))
print('Listening ...')
bot.run()

config.save()
print('Config saved')
