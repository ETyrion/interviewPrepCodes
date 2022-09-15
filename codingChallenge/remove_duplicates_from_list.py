dup_ele_list = [1,1,1,3,4,3,2,5,6,4,5,7]
uniq_list = []

for i in dup_ele_list:
    if i not in uniq_list:
        uniq_list.append(i)

print(sorted(uniq_list))

# sum_list = sum(dup_ele_list)
# print(sum_list)
#
# sum_list_2 = 0
#
# for i in dup_ele_list:
#     sum_list_2=sum_list_2+i
#
# print(sum_list_2)