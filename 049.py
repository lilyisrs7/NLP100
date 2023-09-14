from collections import defaultdict
from itertools import combinations
import re

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

def extract_path_between_nouns(ai):
    paths = []
    for sentence in ai:
        for chunk in sentence:
            if '名詞' in set(map(lambda x: x.pos, chunk.morphs)):
                path = [''.join(['XY' if morph.pos == '名詞' else morph.surface for morph in chunk.morphs if morph.pos != '記号'])]
                while chunk.dst != -1:
                    chunk = sentence[chunk.dst]
                    path.append(''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']))
                paths.append(path)
    path_comb_list = combinations(paths, 2)
    for path_comb in path_comb_list:
        path1, path2 = path_comb
        i = -1
        while len(path1) + i != -1 and len(path2) + i != -1 and path1[i] == path2[i]:
            i -= 1
        if i != -1:
            if len(path1) + i == -1 and len(path2) + i == -1:
                print('X | Y | ' + ' -> '.join(path1[1:]))
            elif len(path1) + i == -1:
                print(re.sub(r'(.*XY)+?', 'X', path2[0]) + ' -> ' + ' -> '.join(path2[1:(i+1)]) + ' -> ' + re.sub(r'(.*XY)+?', 'Y', path2[i+1]))
            elif len(path2) + i == -1:
                print(re.sub(r'(.*XY)+?', 'X', path1[0]) + ' -> ' + ' -> '.join(path1[1:(i+1)]) + ' -> ' + re.sub(r'(.*XY)+?', 'Y', path1[i+1]))
            else:
                print(' -> '.join([re.sub(r'(.*XY)+?', 'X', path1[0])] + path1[1:(i+1)]) + ' | ' + ' -> '.join([re.sub(r'(.*XY)+?', 'Y', path2[0])] + path2[1:(i+1)]) + ' | ' + path1[i+1])
    return

ai = read_ai_chunks('ai.ja.txt.parsed')
extract_path_between_nouns(ai)