from os import walk

directory = '../database/'
for _, _, filenames in walk(directory):
    for filename in filenames:
        with open(directory + filename, 'w') as f:
            f.write(r'{}')