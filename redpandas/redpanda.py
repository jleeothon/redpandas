

__all__ = ['RedPanda']


class RedPanda(object):

    def __init__(self, name, cuteness):
        if not isinstance(cuteness, int):
            raise TypeError("Cuteness is not of type int")
        if cuteness < 2:
            raise ValueError("Red panda is not cute enough")
        self.name = name
        self.cuteness = cuteness

    def say_something_cute(self):
        return "<3" * self.cuteness





