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

def extract_noun_seq(neko):
    for sent in neko:
        noun_seq = []
        for word in sent:
            if word['pos'] == '名詞':
                noun_seq.append(word['surface'])
            else:
                if len(noun_seq) >= 2:
                    print(''.join(noun_seq))
                noun_seq = []
    if len(noun_seq) >= 2:
        print(''.join(noun_seq))
    return

neko = read_neko('neko.txt.mecab')
extract_noun_seq(neko)