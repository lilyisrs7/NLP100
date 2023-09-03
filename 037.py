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

def plot_word_occur_with_neko_top10(neko):
    words = []
    for sent in neko:
        sent_words = [word['surface'] for word in sent]
        if '猫' in sent_words:
            words += sent_words
    words_cnt = Counter(words)
    words_cnt.pop('猫')
    words_sorted = sorted(words_cnt.items(), key=lambda x: x[1], reverse=True)
    plt.bar(*zip(*words_sorted[:10]))
    plt.title('「猫」との共起頻度上位10語')
    plt.xlabel('単語')
    plt.ylabel('「猫」との共起頻度（回）', labelpad=10)
    plt.savefig('037.png')
    return

neko = read_neko('neko.txt.mecab')
plot_word_occur_with_neko_top10(neko)