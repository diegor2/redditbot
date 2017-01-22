import json
import os
import os.path

from collections import defaultdict



class JsonObject(object):

    def __init__(self, json_file, version='0.0'):
        self.file = json_file
        self.data = defaultdict(lambda: None)

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                self.data = json.load(f)
        # TODO: handle versions

    def save(self):
        with open(self.file, 'w') as f:
            f.write(json.dumps(self.data, sort_keys=True, indent=4))

    def __getitem__(self, key):
        if not self.data:
            self.load()
        return self.data[str(key)]

    def __setitem__(self, key, value):
        if not self.data:
            self.load()
        self.data[str(key)] = value

    def __delitem__(self, key):
        if not self.data:
            self.load()
        del self.data[str(key)]

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)

    def _merge(self, old, new):
        for k, v in new.items():
            if isinstance(old.get(k, None), dict):
                old = self._merge(old[k], v)
            else:
                old[k] = v or old[k]
            return old

    def merge(self, new):
        self._merge(self.data, new)


class Config(JsonObject):

    def __init__(self):
        super().__init__('config.json')

    def load(self):
        super().load()
        # Enviroment variables can override json
        self.merge({'clients' :{
            'reddit' : {
                'client_id'     : os.environ.get('TELEGRAM_REDDIT_ID', None),
                'client_secret' : os.environ.get('TELEGRAM_REDDIT_SECRET', None),
                'username'      : os.environ.get('TELEGRAM_REDDIT_USERNAME', None),
                'password'      : os.environ.get('TELEGRAM_REDDIT_PASSWORD', None),
            }, 'telegram': {
                'token'         : os.environ.get('TELEGRAM_REDDIT_TOKEN', None)
            }
        }})
