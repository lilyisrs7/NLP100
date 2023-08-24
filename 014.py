import sys

def head(N, filepath):
    with open(filepath) as f:
        print(''.join([line.rstrip()+'\n' for line in f.readlines()[:N]]), end='')
    return

head(int(sys.argv[1]), 'popular-names.txt')
# check
# python 014.py 5 > 014.txt
# head -5 popular-names.txt > 014_check.txt
# diff 014.txt 014_check.txt