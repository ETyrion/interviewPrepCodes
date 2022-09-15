# numinput = int(input(f'Please provide the number :' ))
# divlist=[]
# for divisor in range(2,numinput):
#     if numinput%divisor==0:
#         divlist.append(divisor)
#
# print(divlist)

# nums= '10,20,30,40,50'
# num_list = nums.split(',')
# print(num_list)
# numstr = ''.join(num_list)
# print(numstr)

# div_list = list(str(div) for div in range(1500,3201) if (div %7==0 and div%5 !=0))
# print(type(div_list))
# print(div_list)
# print(','.join(div_list))

# name_ip = str(input('Please provide name : '))
# name_list = name_ip.split(' ')
# print(name_list)
#
# reversed_list = list(reversed(name_list))
# print(' '.join(reversed_list))

# color_ip = str(input('Please provide color names: '))
# color_list = color_ip.split('-')
# print(color_list)
# sorted_color_list = color_list.sort()
# print('-'.join(color_list))

# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#
# words_len =[(w, len(w)) for w in words]
# # i=0
# #
# # for word_length in words:
# #     length = len(words[i])
# #     words_len.append((words[i], length))
# #     i=i+1
#
# print(words_len)
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# set1= set(words)
# word_len={}
#
# i=0
# for w in words:
#     word_len[w]=len(w)
#
# print(word_len)

# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
#
# word_len_list = [(w, len(w)) for w in words]
# print(word_len_list)

d1 = {'x': 5, 'a': 6, 'c': 12, 'b': 10}

for values in sorted(d1.values()):
    print(f'{values}')
















