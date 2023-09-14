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
    with open(filepath) as f:
        sentence = []
        src_lst = defaultdict(list)
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
                        src_lst = defaultdict(list)
                else:
                    surface = info[0]
                    info_ = info[1].split(',')
                    base = info_[-3]
                    pos = info_[0]
                    pos1 = info_[1]
                    morph = Morph(surface, base, pos, pos1)
                    sentence[-1].morphs = sentence[-1].morphs + [morph]
    return ai

def extract_verb_case_pattern(ai):
    for sentence in ai:
        for i in range(len(sentence)-1):
            chunk_i = sentence[i]
            chunk_i1 = sentence[i+1]
            if len(chunk_i.morphs) == 2:
                morph_0 = chunk_i.morphs[0]
                morph_1 = chunk_i.morphs[1]
                if morph_0.pos == '名詞' and morph_0.pos1 == 'サ変接続' and morph_1.surface == 'を' and morph_1.pos == '助詞':
                    for morph in chunk_i1.morphs:
                        if morph.pos == '動詞':
                            verb = morph_0.base + morph_1.base + morph.base
                            cases = set()
                            chunks = defaultdict(list)
                            for src in chunk_i1.srcs:
                                if src != i:
                                    for src_morph in sentence[src].morphs:
                                        if src_morph.pos == '助詞':
                                            cases.add(src_morph.surface)
                                            chunks[src_morph.surface].append(''.join([src_morph.surface for src_morph in sentence[src].morphs if src_morph.pos != '記号']))
                            if len(cases) > 0:
                                cases = sorted(list(cases))
                                print(verb, ' '.join(cases), ' '.join([' '.join(chunks[src_morph]) for src_morph in cases]), sep='\t')
                            break
    return

ai = read_ai_chunks('ai.ja.txt.parsed')
extract_verb_case_pattern(ai)