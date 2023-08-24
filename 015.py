import sys

def last(N, filepath):
    with open(filepath) as f:
        print(''.join([line.rstrip()+'\n' for line in f.readlines()[-N:]]), end='')
    return

last(int(sys.argv[1]), 'popular-names.txt')
# check
# python 015.py 5 > 015.txt
# tail -5 popular-names.txt > 015_check.txt
# diff 015.txt 015_check.txt