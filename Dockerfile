FROM alpine

RUN apk --update --no-cache add \
      python3 \
      ca-certificates \
      openssl

COPY src /var/local/redditbot
WORKDIR  /var/local/redditbot

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

CMD [ "/usr/bin/python3", "redditbot.py" ]
