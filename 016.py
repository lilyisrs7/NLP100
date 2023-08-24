import sys
import os

def split(N, filepath):
    with open(filepath) as f:
        lines = f.readlines()
    line_per_file = len(lines) // N
    for i in range(N):
        filename = filepath[:-4]+'-'+str(i+1)+'.txt'
        if os.path.isfile(filename):
            mode = 'w'
        else:
            mode = 'x'
        with open(filename, mode=mode) as f:
            if i != N-1:
                f.write(''.join(lines[line_per_file*i:line_per_file*(i+1)]))
            else:
                f.write(''.join(lines[line_per_file*i:]))
    return

split(int(sys.argv[1]), 'popular-names.txt')
# check
# python 016.py 5
# split -d -l 556 popular-names.txt popular-names
# diff popular-names-1.txt popular-names00
# diff popular-names-2.txt popular-names01
# diff popular-names-3.txt popular-names02
# diff popular-names-4.txt popular-names03
# diff popular-names-5.txt popular-names04