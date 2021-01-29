# put your code here
# word_count = {}
# file = open('test.txt')
# my_list = []
# for line in file:
#     line = line.rstrip()
#     my_list[len(my_list):len(my_list)]=line.split(" ")
# for word in my_list:
#     if word[-1] in [",", ".", "?"]:
#         word = word[0:-1]
#     word_count[word.lower()] =  word_count.get(word.lower(), 0) + 1
# for word, count in word_count.items():
#     print(f'{word} {count}')

# the code using counter
import collections
word_count = {}
file = open('test.txt')
my_list = []
for line in file:
    line = line.rstrip()
    my_list[len(my_list):len(my_list)]=line.split(" ")

c = collections.Counter(my_list)
for word, count in c.items():
    print(f'{word} {count}')
