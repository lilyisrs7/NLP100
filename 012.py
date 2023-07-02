import os

def extract_col12(filepath):
    with open(filepath) as f:
        all = f.readlines()
        if os.path.isfile('col1.txt'):
            mode1 = 'w'
        else:
            mode1 = 'x'
        if os.path.isfile('col2.txt'):
            mode2 = 'w'
        else:
            mode2 = 'x'
        with open('col1.txt', mode=mode1) as f1:
            f1.write(''.join([line.rstrip().split('\t')[0]+'\n' for line in all]))
        with open('col2.txt', mode=mode2) as f2:
            f2.write(''.join([line.rstrip().split('\t')[1]+'\n' for line in all]))
    return

extract_col12('popular-names.txt')
# check
# cut -f 1 -d $'\t' popular-names.txt > col1_check.txt
# cut -f 2 -d $'\t' popular-names.txt > col2_check.txt
# diff col1_check.txt col1.txt
# diff col2_check.txt col2.txt