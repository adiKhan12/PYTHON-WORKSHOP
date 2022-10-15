# lets say i want to create a list of lengths of the words in a list

# 1st method
my_word = ['hello', 'world', 'this', 'is', 'a', 'list', 'comprehension']

word_len = []

for word in my_word:
    word_len.append(len(word))

print("1st method:", word_len)

# 2nd method
word_len = [len(word) for word in my_word]

print("2nd method:", word_len)

# we can use conditions in list comprehension

word_len = [len(word) for word in my_word if(len(word) > 3)]

print("With Condition method:", word_len)