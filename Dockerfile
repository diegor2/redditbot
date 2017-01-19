FROM python:alpine

COPY src /var/local/redditbot
WORKDIR  /var/local/redditbot

RUN pip3 install -r requirements.txt

CMD [ "python", "bot.py" ]
