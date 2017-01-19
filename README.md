To run using Docker:
---

    docker build -t redditbot .
    docker run --rm -it \
      -e "TELEGRAM_REDDIT_TOKEN=Telegram bot token" \
      -e "TELEGRAM_REDDIT_ID=Reddit app id" \
      -e "TELEGRAM_REDDIT_SECRET=Reddit app secret" \
      -e "TELEGRAM_REDDIT_USERNAME=Reddit bot username" \
      -e "TELEGRAM_REDDIT_PASSWORD=Reddit bot password" \
      redditbot

To run on the host machine (need python 3.x):
---

    pip3 install -r requirements.txt
    python3 bot.py

APIs
---

To get a Telegram bot token:
  Go to https://telegram.me/botfather to talk to @botfather and send /newbot

To create reddit user and password for your bot:
  Go to https://www.reddit.com/login and create an account

To get the Reddit app id and secret:
  Go to https://www.reddit.com/prefs/apps and click "create another app"
