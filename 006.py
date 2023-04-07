def char_ngram(sentence, n):
    return [sentence[i:i+n] for i in range(len(sentence)-n+1)]

X = set(char_ngram("paraparaparadise", 2))
Y = set(char_ngram("paragraph", 2))
print('union: ', set.union(X, Y))
print('intersection: ', set.intersection(X, Y))
print('X/Y: ', set.difference(X, Y))
print('Y/X: ', set.difference(Y, X))
if 'se' in X:
    print('\'se\' is in X')
else:
    print('\'se\' is not in X')
if 'se' in Y:
    print('\'se\' is in Y')
else:
    print('\'se\' is not in Y')