import json
import os

def _json_load(filename):
    try:
        with open(filename) as f:
            return json.loads(f.read())
    except:
        print("Failed to load json '{}', returning empty list...".format(filename))
        return []

def load(classname):
    filename = 'database/{}.json'.format(classname)
    if not os.path.exists(filename):
        print("'{}' does not exist, returning empty list...".format(classname))
        return []

    return _json_load(filename)

def commit(obj, classname):
    filename = 'database/{}.json'.format(classname)
    try:
        if not os.path.exists(filename):
            print("'{}' does not exist...".format(classname))
            return False
        with open(filename) as f:
            f.write(json.dumps(obj))
        return True
    except:
        print("Commit with {}, {} has failed...".format(obj, classname))
        return False