from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib

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

def plot_word_freq_hist(neko):
    words = []
    for sent in neko:
        words += [word['surface'] for word in sent]
    words_cnt = Counter(words)
    words_sorted = sorted(words_cnt.items(), key=lambda x: x[1], reverse=True)
    plt.hist(list(map(lambda x: x[1], words_sorted)), bins=100)
    plt.title('出現頻度')
    plt.xlabel('出現頻度')
    plt.ylabel('その頻度で出現する単語数')
    plt.savefig('038.png')
    return

neko = read_neko('neko.txt.mecab')
plot_word_freq_hist(neko)