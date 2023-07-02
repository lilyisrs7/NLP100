def replace_tab(filepath):
    with open(filepath) as f:
        print(f.read().rstrip().replace('\t', ' '))
    return

replace_tab('popular-names.txt')
# check
# sed -e "s/\t/ /g" popular-names.txt > 011_check.txt
# python 011.py > 011.txt
# diff 011_check.txt 011.txt