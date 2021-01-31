# put your code here
import sys
import string
file = open(sys.argv[1])
word_count = {}
tokens = []
for line in file:
    line = line.rstrip()
    words = line.split()

    for word in words:
        word = word.strip(string.punctuation)
        word = word.lower()
        tokens.append(word)

for word in tokens:
    word_count[word] =  word_count.get(word , 0) + 1
for word, count in word_count.items():
    print(f'{word} {count}')

