import random

def shuffle(string):
    words = string.split(' ')
    shuffled = []
    for word in words:
        if len(word) <= 4:
            shuffled.append(word)
        else:
            new_word = word[0] + ''.join(random.sample(word[1:-1], len(word)-2)) + word[-1]
            shuffled.append(new_word)
    return ' '.join(shuffled)

print(shuffle('I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'))