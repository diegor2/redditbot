import praw
import clients

from collections import defaultdict

USER_AGENT = 'telegram:br.net.ruggeri.telegram-link:0.1 (by /u/diegor2)'

class RedditBot(object):

    def __init__(self, **kwargs):
        self.reddit = praw.Reddit(user_agent=USER_AGENT, **kwargs)

    def exists(self, subreddit):
        return bool(list(self.reddit.subreddits.search(subreddit)))

    def submit(self, subreddit, title, url):
        sub = self.reddit.subreddit(subreddit)
        sub.submit(title, url=url, send_replies=False)
