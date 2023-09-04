from collections import defaultdict

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

def read_ai_chunks(filepath):
    ai = []
    src_lst = defaultdict(list)
    with open(filepath) as f:
        sentence = []
        for line in f.readlines():
            if line.startswith('*'):
                info = line.split()
                dst = int(info[2][:-1])
                src = int(info[1])
                src_lst[dst] = src_lst[dst]+[src]
                chunk = Chunk([], dst, src_lst[src])
                sentence.append(chunk)
            else:
                info = line.rstrip().split('\t')
                if info[0] == 'EOS':
                    if sentence != [] and sentence[-1].morphs != []:
                        ai.append(sentence)
                        sentence = []
                else:
                    surface = info[0]
                    info_ = info[1].split(',')
                    base = info_[-3]
                    pos = info_[0]
                    pos1 = info_[1]
                    morph = Morph(surface, base, pos, pos1)
                    sentence[-1].morphs = sentence[-1].morphs + [morph]
    return ai

def extract_noun_to_verb_dep(ai):
    for sentence in ai:
        for chunk in sentence:
            if chunk.dst != -1 and '名詞' in set(map(lambda x: x.pos, chunk.morphs)) and '動詞' in set(map(lambda x: x.pos, sentence[chunk.dst].morphs)):  
                src = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
                dst = ''.join([morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号'])
                print(src, dst, sep='\t')
    return

ai = read_ai_chunks('ai.ja.txt.parsed')
extract_noun_to_verb_dep(ai)