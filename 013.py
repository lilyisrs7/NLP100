import os

def merge(filepath1, filepath2):
    with open(filepath1) as f1:
        all1 = f1.readlines()
        with open(filepath2) as f2:
            all2 = f2.readlines()
            if os.path.isfile('merged.txt'):
                mode = 'w'
            else:
                mode = 'x'
            with open('merged.txt', mode=mode) as f:
                f.write(''.join([text1.rstrip()+'\t'+text2.rstrip()+'\n' for text1, text2 in zip(all1, all2)]))
    return

merge('col1.txt', 'col2.txt')
# check
# paste -d $'\t' col1.txt col2.txt > merged_check.txt
# diff merged.txt merged_check.txt