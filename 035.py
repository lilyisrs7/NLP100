from collections import Counter

def read_neko(filepath):
    neko = []
    with open(filepath) as f:
        sentence = []
        for line in f.readlines():
            info = line.rstrip().split('\t')
            if info[0] == '\u3000' or info[0] == 'EOS':
                if sentence != []:
                    neko.append(sentence)
                    sentence = []
            else:
                word = {}
                word['surface'] = info[0]
                word['base'] = info[3]
                pos_info = info[4].split('-')
                if len(pos_info) >= 1:
                    word['pos'] = pos_info[0]
                else:
                    word['pos'] = '-'
                if len(pos_info) >= 2:
                    word['pos1'] = pos_info[1]
                else:
                    word['pos1'] = '-'
                sentence.append(word)
                if info[0] == ('。'):
                    neko.append(sentence)
                    sentence = []
    return neko

def word_freq(neko):
    words = []
    for sent in neko:
        words += [word['surface'] for word in sent]
    words_cnt = Counter(words)
    words_sorted = sorted(words_cnt.items(), key=lambda x: x[1], reverse=True)
    for word in words_sorted:
        print(word)
    return

neko = read_neko('neko.txt.mecab')
word_freq(neko)