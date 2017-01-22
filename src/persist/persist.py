import json
import os
import os.path

from collections import defaultdict
from persist.decorators import lazy

class JsonObject(object):

    def __init__(self, json_file, version='0.0'):
        self.file = json_file
        self.data = {}

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                self.data = json.load(f)
        # TODO: handle versions

    def save(self):
        with open(self.file, 'w') as f:
            f.write(json.dumps(self.data, sort_keys=True, indent=4))

    @lazy
    def merge(self, new):
        self._merge(self.data, new)

    @lazy
    def __getitem__(self, key):
        return self.data.get(str(key), None)

    @lazy
    def __setitem__(self, key, value):
        self.data[str(key)] = value

    @lazy
    def __delitem__(self, key):
        self.data.pop(str(key), None)

    @lazy
    def __repr__(self):
        return repr(self.data)

    @lazy
    def __str__(self):
        return str(self.data)

    def _merge(self, old, new):
        for k, v in new.items():
            if isinstance(old.get(k, None), dict):
                old = self._merge(old[k], v)
            else:
                old[k] = v or old[k]
            return old


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
