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

def extract_noun_phrase_connected_by_of(neko):
    for sent in neko:
        for i in range(len(sent)-2):
            if sent[i]['pos'] == '名詞' and sent[i+1]['surface'] == 'の' and sent[i+2]['pos'] == '名詞':
                print(''.join(map(lambda x: x['surface'], sent[i:i+3])))
    return

neko = read_neko('neko.txt.mecab')
extract_noun_phrase_connected_by_of(neko)