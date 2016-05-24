from json import loads

def parse (filepath):
    CONTENT = ''
    with open (filepath, 'r') as f:
        for i in f.readlines ():
            CONTENT += i
    return loads (CONTENT)