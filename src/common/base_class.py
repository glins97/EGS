import types
import json

class BaseClass(object):
    def __init__(self, *args, **kwargs):
        self.pks = ['code']

    def serialyze(self):
        res = {}
        for attr in dir(self):
            if attr != 'pks' and '__' not in attr[:2] and '__' not in attr[-2:] and type(getattr(self, attr)) != types.MethodType:
                res[attr] = getattr(self, attr)
        return res

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            for pk in self.pks:
                if getattr(self, pk) != getattr(other, pk):
                    return False
            return True

        if isinstance(other, dict):
            for pk in self.pks:
                if getattr(self, pk) != other[pk]:
                    return False
            return True

        return False