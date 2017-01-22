def lazy(func):
    def wrapper(self, *args):
        if not self.data:
            self.load()
        return func(self, *args)
    return wrapper
