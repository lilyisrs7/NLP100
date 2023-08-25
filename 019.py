from collections import Counter

def sortcol1(filepath):
    with open(filepath) as f:
        col1_all = [line.rstrip().split()[0] for line in f.readlines()]
        print('\n'.join(map(lambda x: x[0], sorted(Counter(col1_all).items(), key=lambda x: x[1], reverse=True))), end='')
    return

sortcol1('popular-names.txt')
# check
# python 019.py > 019.txt
# cut -f 1 popular-names.txt | sort | uniq -c | sort -n -r | cut -c 6- > 019_check.txt