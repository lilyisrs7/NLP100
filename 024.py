import re

def extract_url(filepath):
    with open(filepath) as f:
        for m in re.findall(r'\[\[ファイル:(.*?)[\|\]]', f.read()):
            print(m)
    return

extract_url('britain.txt')