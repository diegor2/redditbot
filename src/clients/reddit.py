import praw
import clients

from clients.abc import Publisher
from collections import defaultdict


USER_AGENT = 'telegram:br.net.ruggeri.telegram-link:0.1 (by /u/diegor2)'


class RedditBot(Publisher):

    def __init__(self, **kwargs):
        self.reddit = praw.Reddit(user_agent = USER_AGENT, **kwargs)
        self.subs = defaultdict(str)

    def publish(self):
        pass

    def submit(self, chat, title, url):
        sub = self.sub[chat] or self.ask_subreddit()

    def ask_subreddit(self):
        telegram = clients.get('telegram')
        telegram.ask_subreddit()
