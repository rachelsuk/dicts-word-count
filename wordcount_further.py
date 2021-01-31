# put your code here
import sys
import string
file = open(sys.argv[1])
tokens = []
for line in file:
    line = line.rstrip()
    words = line.split()

    for word in words:
        word = word.strip(string.punctuation)
        word = word.lower()
        tokens.append(word)

print(tokens)

