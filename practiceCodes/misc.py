# div_list= list()
#
# for i in range(1500, 3201):
#     if i%7 ==0 and i%5!=0:
#         div_list.append(str(i))
#
# str_div_list = ','.join(div_list)
# print(str_div_list)

# user_ip_string = str(input('Enter the string: '))
#
# list_string = user_ip_string.split()
# print(list_string)
#
# rev_str = list_string[::-1]
# print(' '.join(rev_str))

# hyphenated_string_ip = 'Red-Green-Black-White'
# hyphenated_string_ip_list = hyphenated_string_ip.split('-')
# hyphenated_string_ip_list.sort()
# print('-'.join(hyphenated_string_ip_list))

# ip_str = 'Hello There you'
# ip_str_list = ip_str.split()
# print(ip_str_list)
# for i in range(len(ip_str_list)-1):
#     ip_str_list[i] = ip_str_list[i][::-1]
#
# print(ip_str_list)
# print(' '.join(ip_str_list))

# words= ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# words.sort()
#
# words_len = list()
#
# for i in words:
#     length = len(i)
#     words_len.append((i, length))
#
# print(words_len)

# names = ["Dan", "John", "Diana"]
# phones = [11111, 2222, 3333]
#
# name_and_phones = set(zip(names, phones))
# print(name_and_phones)

# listA = ['A', 'B', 'C', 'D']
# listB = ['E', 'B', 'C', 'F']
# listC = list(set(listA) & set(listB))
# print(listC)

dictA =  {'x': 5, 'a': 3, 'c': 2, 'b': 0}

dict_keys = dictA.keys()

for i in sorted(dict_keys):
    print(f'{i} , {dictA[i]}')

dict_values = dictA.values()

for i in sorted(dictA.items()):
    print(i)





