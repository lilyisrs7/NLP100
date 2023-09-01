import re

def extract_template(filepath):
    basicinfo = {}
    with open(filepath) as f:
        m = re.findall(r'\{\{基礎情報(.*?\n\}\})', f.read(), re.S)
        assert len(m) == 1
        for item in re.findall(r'\n\|(.*?)(?=(\n\||\n\}\}))', m[0], re.S):
            field, val = re.search(r'(.*?)\=(.*)', item[0], re.S).groups()
            field = re.sub(r'\s*(.*?)\s*', r'\1', field)
            val = re.sub(r'(?:(?!\n)\s)*(.*?)(?:(?!\n)\s)*', r'\1', val, flags=re.S)
            basicinfo[field] = val
    for k, v in basicinfo.items():
        print(k, ':', v)
    return

extract_template('britain.txt')