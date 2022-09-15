orig_str = str(input('Please provide a string: '))
orig_list_str = orig_str.split()
rev_list =[]
print(orig_list_str)
i=0
for words in orig_list_str:
    rev_list.append(words[::-1])

    #i = i+1
    # orig_list_str[i] = words[::-1]
    # print(orig_list_str)
    # i = i+1
print(rev_list)


# reversed_str= ' '.join(orig_list_str)
#
# print(reversed_str)

