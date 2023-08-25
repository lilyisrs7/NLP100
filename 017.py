def col1(filepath):
    with open(filepath) as f:
        col1set = set([line.rstrip().split()[0]+'\n' for line in f.readlines()])
        print(''.join(sorted(list(col1set))), end='')
    return

col1('popular-names.txt')
# check
# python 017.py > 017.txt
# cut -f 1 popular-names.txt | sort -u -o 017_check.txt
# diff 017.txt 017_check.txt