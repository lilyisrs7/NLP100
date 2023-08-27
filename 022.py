import re

def extract_category(filepath):
    with open(filepath) as f:
        for line in f.readlines():
            if re.match(r'\[\[Category:.*\]\]', line):
                print(line.rstrip()[11:-2])
    return

extract_category('britain.txt')