import re
import requests

def extract_flag_url(filepath):
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
            new_val = re.sub(r'\[(http.*?)\]', r'\1', new_val)
            new_val = re.sub(r'^\*+', r'', new_val, flags=re.M)
            new_val = re.sub(r'<ref>(.*?)</ref>', r'\1', new_val, flags=re.S)
            new_val = re.sub(r'<(ref name=(?:.*?))>(.*?)</ref>', r'\1\2', new_val, flags=re.S)
            new_val = re.sub(r'<(ref name=(?:.*?)) />', r'\1', new_val, flags=re.S)
            new_val = re.sub(r'<br />', r'', new_val)
            new_val = re.sub(r'\[\[(ファイル:.*?)\]\]', r'\1', new_val)
            new_val = re.sub(r'\{\{(Cite web\|.*?)\}\}', r'\1', new_val, flags=re.M)
            new_val = re.sub(r'\{\{(?:(?:(?!\}\}).)*?\|)+(.*?)\}\}', r'\1', new_val)
            new_val = re.sub(r'\{\{(.*?)\}\}', r'\1', new_val)
            basicinfo[new_field] = new_val
    fig_name = basicinfo.get('国旗画像')
    
    S = requests.Session()
    URL = 'https://www.mediawiki.org/w/api.php'
    PARAMS = {
        'action': 'query',
        'format': 'json',
        'prop': 'imageinfo',
        'titles': 'File:' + fig_name,
        'iiprop': 'url'
    }
    data = S.get(url=URL, params=PARAMS).json()
    pages = data['query']['pages']
    for v in pages.values():
        print(v['imageinfo'][0]['url'])
    return

extract_flag_url('britain.txt')