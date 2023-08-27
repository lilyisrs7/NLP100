import json
import os

def load(filepath):
    d = [json.loads(line) for line in open(filepath)]
    britain = list(filter(lambda x: x['title'] == 'イギリス', d))
    assert len(britain) == 1
    writefile = 'britain.txt'
    if os.path.isfile(writefile):
        mode = 'w'
    else:
        mode = 'x'
    with open(writefile, mode=mode) as f:
        f.write(britain[0]['text'])
    return

load('jawiki-country.json')