from abc import ABCMeta, abstractmethod

class Chatter(metaclass=ABCMeta):

    @abstractmethod
    def ask_topic(self):
        pass


class Publisher(metaclass=ABCMeta):

    @abstractmethod
    def publish(self):
        pass
