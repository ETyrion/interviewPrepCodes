words = input(str('Provide the words '))
words_list = words.split(' ')

print(words_list)

reversed_list = ' '.join(reversed(words_list))
print(reversed_list)