from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import math

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

def plot_word_freq_zipf(neko):
    words = []
    for sent in neko:
        words += [word['surface'] for word in sent]
    words_cnt = Counter(words)
    words_sorted = sorted(words_cnt.values(), reverse=True)
    plt.scatter([math.log(i) for i in range(1, len(words_sorted)+1)], [math.log(i) for i in words_sorted])
    plt.title('出現頻度順位と出現頻度の関係')
    plt.xlabel('log出現頻度順位')
    plt.ylabel('log出現頻度（回）')
    plt.savefig('039.png')
    return

neko = read_neko('neko.txt.mecab')
plot_word_freq_zipf(neko)