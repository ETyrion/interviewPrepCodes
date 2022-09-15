############ List Methods #########
num_list = [1,2,3,4]
print(num_list)

num_list.insert(1,6)
print(num_list)

num_list.insert(2,5)

print(num_list)

num_list.insert(0,[1,2])
print(num_list)

num_list.insert(0, 1)

print(num_list)

################ To append at the end of list ######################

num_list_end = num_list

print(num_list_end)
num_list_end.append(9)
print(num_list_end )

num_list_end.pop()
print(num_list_end)

num_list_end.pop()
print(num_list_end)

num_list_end.pop(3)

print(num_list_end)

names = ['Bob', 'Alice', 'Daryl']

names_str = ','.join(names)
print(names_str)

# Insert method exercise

animals = ['Cat', 'Dog']
animals.append('Donkey')
print(animals)
animals.insert(1, 'Horse')
print(animals)
cat_val = animals.index('Cat')
print(cat_val)

# To get the count of any item

numerals = [1,2,1,3,4,1,1,2,3,2]

print(numerals.count(2))

# Converting string to a list

# Transform a space separated string to hyphenated string

str = 'I Love Python programming'

lst_str = str.split(' ')
print(lst_str)

hyphenated_str = '-'.join(lst_str)

print(hyphenated_str)

#