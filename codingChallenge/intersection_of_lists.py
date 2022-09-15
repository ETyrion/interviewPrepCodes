list1 = [1,2,3,4,5]
list2 = [3,4,6,8,9,5]

list3 = list(set(list1).intersection(set(list2)))
print(list3)
print(type(list3))