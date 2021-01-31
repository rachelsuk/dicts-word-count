# put your code here
import sys
import string
import collections
file = open(sys.argv[1])

tokens = []
for line in file:
    line = line.rstrip()
    words = line.split()

    for word in words:
        word = word.strip(string.punctuation)
        word = word.lower()
        tokens.append(word)
word_count = collections.Counter(tokens)
sorted_word_count = sorted(word_count)

for word in sorted_word_count:
    print(f'{word} {word_count[word]}')

