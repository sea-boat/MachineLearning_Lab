import random

words = ["中", "国", "人", "中", "午", "要", "吃", "午", "饭"]
cache = {}
size = 3


def binary():
    for i in range(len(words) - 1):
        yield (words[i], words[i + 1])


for w1, w2 in binary():
    key = w1
    if key in cache:
        cache[key].append(w2)
    else:
        cache[key] = [w2]

seed = random.randint(0, len(words) - 1)
seed_word = words[seed]
word1 = seed_word
_words = []
for i in range(size):
    _words.append(word1)
    word1, = random.choice(cache[word1])
print(' '.join(_words))
