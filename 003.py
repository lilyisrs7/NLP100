sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sentence.replace(',', '').split(' ')
print([len(word)-1 if word.endswith('.') else len(word) for word in words]) # .は語尾以外の場所にあった場合は文字数に含める