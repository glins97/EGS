import types
import json

class BaseClass(object):
    def serialyze(self):
        res = {}
        for attr in dir(self):
            if '__' not in attr[:2] and '__' not in attr[-2:] and type(getattr(self, attr)) != types.MethodType:
                res[attr] = getattr(self, attr)
        return json.dumps(res)