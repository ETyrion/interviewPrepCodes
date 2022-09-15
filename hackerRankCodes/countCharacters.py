# def count_char(name_str):
#     count_dict = {}
#
#     for c in name_str:
#         if c == ' ':
#             pass
#         elif c in count_dict:
#             count_dict[c] = count_dict[c]+1
#         else:
#             count_dict[c] = 1
#     return count_dict
#
# char_count = count_char('ABHISHEK MISHRA')
# print(char_count)
from collections import Counter
def count_char(name_str):
    return Counter(name_str)

name = "Hacker Rank"
count_char(name)
print(count_char(name))