sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split(' ')
dic = {}
for i, word in enumerate(words):
    if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
        dic[word[0]] = i+1
    else:
        dic[word[:2]] = i+1
print(dic)