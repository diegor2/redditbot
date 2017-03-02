To run using Docker:
---

    docker run --rm -it \
      -v "$PWD/chats.json:/var/local/redditbot/chats.json" \
      -v "$PWD/config.json:/var/local/redditbot/config.json" \
      -e "TELEGRAM_REDDIT_TOKEN=Telegram bot token" \
      -e "TELEGRAM_REDDIT_ID=Reddit app id" \
      -e "TELEGRAM_REDDIT_SECRET=Reddit app secret" \
      -e "TELEGRAM_REDDIT_USERNAME=Reddit bot username" \
      -e "TELEGRAM_REDDIT_PASSWORD=Reddit bot password" \
      diegor2/redditbot

    Mapping volumes is optional. Use if you need to persist configuration.

To build
---

    docker build -t diegor2/redditbot .

Building is also optional. If you execute just the `docker run` command above,
it will use the [image from the docker hub](https://hub.docker.com/r/diegor2/redditbot/).

To run without a container (need python 3.x):
---

Copy `config.json.example` to `config.json` file and fill with the API tokens.

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
