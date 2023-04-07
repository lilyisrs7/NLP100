def word_ngram(sentence, n):
    words = sentence.split(' ')
    return [words[i:i+n]for i in range(len(words)-n+1)]

def char_ngram(sentence, n):
    return [sentence[i:i+n] for i in range(len(sentence)-n+1)]

print(word_ngram("I am an NLPer", 2))
print(char_ngram("I am an NLPer", 2))