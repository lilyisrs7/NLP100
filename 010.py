def count_lines(filepath):
    with open(filepath) as f:
        print(len(f.readlines()))
    return

count_lines('popular-names.txt')
# check
# wc -l popular-names.txt
# python 010.py