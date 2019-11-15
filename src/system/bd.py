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

def _infer_classname(obj):
    return obj.__class__.__name__.lower() + 's'

def auth(cpf, password, data):
    cpf = cpf.replace('-', '').replace('.', '')
    for user in data:
        if user['user_cpf'].replace('-', '').replace('.', '') == cpf and user['password'] == password:
            return True
    return False  

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
            f.write(json.dumps(data, cls=Encoder, indent=4))
        return True
    except:
        print("Commit with data='{}' classname='{}' has failed...".format(data, classname))
        return False

# obj = obj to be appended
# data = list of objs of that class
#   normally obtained thru a 'load' call with 
#   appropriate classname
# if classname is not specified, it will be inferred
def append(obj, data, classname=None):
    if classname is None:
        classname = _infer_classname(obj)
        
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
# if classname is not specified, it will be inferred
def update(obj, data, classname=None):
    if classname is None:
        classname = _infer_classname(obj)

    has_update = False
    for index, item in enumerate(data):
        if item == obj:
            data[index] = obj
            has_update = True
    
    if has_update:
        commit(data, classname)
    else:
        print('Cannot update database: no object matches specified private key')

# attrs = dict of attributes that must match
# data = table data 
def select(attrs, data):
    target = len(attrs)
    matches = 0
    results = []
    for item in data:
        for attr in attrs:
            if item[attr] == attrs[attr] or attrs[attr] == '':
                matches += 1
        if matches == target:
            results.append(item)
    return results