import re

def extract_category_lines(filepath):
    with open(filepath) as f:
        for line in f.readlines():
            if re.match(r'\[\[Category', line):
                print(line.rstrip())
    return

extract_category_lines('britain.txt')