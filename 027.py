import re

def extract_template_remove_markup(filepath):
    basicinfo = {}
    with open(filepath) as f:
        m = re.findall(r'\{\{基礎情報(.*?\n\}\})', f.read(), re.S)
        assert len(m) == 1
        for item in re.findall(r'\n\|(.*?)(?=(\n\||\n\}\}))', m[0], re.S):
            field, val = re.search(r'(.*?)\=(.*)', item[0], re.S).groups()
            field = re.sub(r'\s*(.*?)\s*', r'\1', field)
            field = re.sub(r'\'{2,5}', r'', field)
            new_field = ''
            replace = list(re.finditer(r'\[\[(?!ファイル)(.*?)\]\]', field))
            if len(replace) == 0:
                new_field = field
            else:
                start = 0
                for pattern in replace:
                    span = pattern.span()
                    replaced = re.sub(r'\[\[(.*?\|)?(.*)\]\]', r'\2', pattern.group())
                    new_field += field[start:span[0]] + replaced
                    start = span[1]
                new_field += field[start:]
            val = re.sub(r'^(?:(?!\n)\s)*(.*?)(?:(?!\n)\s)*$', r'\1', val, flags=(re.S|re.M))
            val = re.sub(r'\'{2,5}', r'', val)
            new_val = ''
            replace = list(re.finditer(r'\[\[(?!ファイル)(.*?)\]\]', val))
            if len(replace) == 0:
                new_val = val
            else:
                start = 0
                for pattern in replace:
                    span = pattern.span()
                    replaced = re.sub(r'\[\[(.*?\|)?(.*)\]\]', r'\2', pattern.group())
                    new_val += val[start:span[0]] + replaced
                    start = span[1]
                new_val += val[start:]
            basicinfo[new_field] = new_val
    for k, v in basicinfo.items():
        print(k, ':', v)
    return

extract_template_remove_markup('britain.txt')