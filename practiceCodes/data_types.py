# Exercise on list data type
'''List data type is just like an array but it supports different data types'''

values = [1,2,"abc", 4.5]

print(values[2])

# print directly the last value of the list

print(values[-1])

# inserting value in between of the list

values.insert(2, 4)

# inserting values at the end of the list

values.append(345)

print(values)

print(len(values))

# deleting the values from list
del values[-1]

print(values)

str = [1, "Python", True, 65]

print(str[2:])
