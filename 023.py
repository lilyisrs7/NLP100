import re

def extract_section(filepath):
    with open(filepath) as f:
        for m in re.findall(r'={2,}.*={2,}', f.read()):
            level = 1
            while m[level+1] == '=' and m[-level-2] == '=':
                level += 1
            m = re.sub(r'\s*(.*?)\s*', r'\1', m[level+1:-level-1])
            print(m, level)
    return

extract_section('britain.txt')