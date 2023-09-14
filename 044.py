import pydot
from collections import defaultdict

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self, morphs, dst, srcs, idx):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
        self.idx = idx

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
                chunk = Chunk([], dst, src_lst[src], src)
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

def draw_dependency_tree(sentence):
    graph = pydot.Dot('dependency_tree', graph_type='digraph')
    for chunk in sentence:
        src = str(chunk.idx) + '.' + ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])
        src_node = pydot.Node(src)
        graph.add_node(src_node)
        dst = ''.join([morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != '記号' and chunk.dst != -1])
        if dst != '':
            dst = str(sentence[chunk.dst].idx) + '.' + dst
            dst_node = pydot.Node(dst)
            graph.add_node(dst_node)
            edge = pydot.Edge(src, dst)
            graph.add_edge(edge)
    graph.write_png('044.png')
    return

ai = read_ai_chunks('ai.ja.txt.parsed')
draw_dependency_tree(ai[1])