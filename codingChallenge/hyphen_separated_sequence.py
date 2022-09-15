sequence_of_words = str(input('Please provide the words list : '))

sequence_list = sequence_of_words.split('-')
print(sequence_list)
sequence_list.sort()
print(sequence_list)
print('-'.join(sequence_list))
