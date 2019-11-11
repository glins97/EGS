import json
import os

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'serialyze'):
            return obj.serialyze()
        return json.JSONEncoder.default(self, obj)

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

def commit(data, classname):
    filename = 'database/{}.json'.format(classname)
    try:
        if not os.path.exists(filename):
            print("'{}' does not exist...".format(classname))
            return False
        with open(filename, 'w') as f:
            f.write(json.dumps(data, cls=Encoder))
        return True
    except:
        print("Commit with data='{}' classname='{}' has failed...".format(data, classname))
        return False

# obj = obj to be appended
# data = list of objs of that class
#   normally obtained thru a 'load' call with 
#   appropriate classname
def append(obj, data, classname):
    is_unique = True
    for item in data:
        if item == obj:
            is_unique = False

    if is_unique:
        data.append(obj)
        commit(data, classname)
    else:
        print('Cannot append object: private key already in database')

# obj = obj to be changed;
#   obj must maintain current pks <--- important
# data = list of objs of that class
#   normally obtained thru a 'load' call with 
#   appropriate classname
def update(obj, data, classname):
    has_update = False
    for index, item in enumerate(data):
        if item == obj:
            data[index] = obj
            has_update = True
    
    if has_update:
        commit(data, classname)
    else:
        print('Cannot update database: no object matches specified private key')
