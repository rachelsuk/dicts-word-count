# put your code here.
word_count = {}
file = open('test.txt')
my_list = []
for line in file:
    line = line.rstrip()
    my_list[len(my_list):len(my_list)]=line.split(" ")
for word in my_list:
    word_count[word] =  word_count.get(word , 0) + 1
for word, count in word_count.items():
    print(f'{word} {count}')


