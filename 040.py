class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def read_ai_morphs(filepath):
    ai = []
    with open(filepath) as f:
        sentence = []
        for line in f.readlines():
            if line.startswith('*'):
                continue
            info = line.rstrip().split('\t')
            if info[0] == 'EOS':
                if sentence != []:
                    ai.append(sentence)
                    sentence = []
            else:
                surface = info[0]
                info_ = info[1].split(',')
                base = info_[-3]
                pos = info_[0]
                pos1 = info_[1]
                morph = Morph(surface, base, pos, pos1)
                sentence.append(morph)
    for morph in ai[1]:
        print(morph.surface, morph.base, morph.pos, morph.pos1)
    return

read_ai_morphs('ai.ja.txt.parsed')