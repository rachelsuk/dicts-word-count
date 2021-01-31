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

for word,count in reversed(sorted(word_count.items(), key=lambda item: item[1])):  
    print(f'{word} {word_count[word]}')

