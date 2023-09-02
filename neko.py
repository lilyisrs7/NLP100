import MeCab
import os

def tokenize(filepath):
    with open(filepath) as f:
        wakati = MeCab.Tagger('-r ../../opt/anaconda3/lib/python3.8/site-packages/unidic_lite/dicdir/mecabrc -d ../../opt/anaconda3/lib/python3.8/site-packages/unidic_lite/dicdir')
        writefile = 'neko.txt.mecab'
        if os.path.isfile(writefile):
            mode = 'w'
        else:
            mode = 'x'
        with open(writefile, mode=mode) as fw:
            fw.write(wakati.parse(f.read()))
    return

tokenize('neko.txt')