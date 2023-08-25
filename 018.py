def sortcol3(filepath):
    with open(filepath) as f:
        print(''.join(sorted(f.readlines(), key=lambda x: int(x.rstrip().split()[2]), reverse=True)), end='')
    return

sortcol3('popular-names.txt')
# check
# python 018.py > 018.txt
# sort -k 3 -n -r popular-names.txt -o 018_check.txt