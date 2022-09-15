word_list = 'I learn Python programming!'.split()
info = [[w.upper(), w.lower(), len(w)] for w in word_list]
print(info)


my_tuple = tuple("I-love-Python")
my_tuple=my_tuple[::]
print(my_tuple)
print(my_tuple[::3])

t5= (1, 3.2, 'a-b-c')
print(t5)
print(t5[-1:0]) # => ('abc', 3.2)


languages = ('Python', 'Java', 'Go', 'C++', 'PHP', 'Scala', 'Solidity')

## Using a negative index extract the last element of the tuple in a variable called x
x = languages[-1]
print(x)

## Return a new tuple called y using slicing and a step
## y should be ('Python', 'Scala')
y = languages[::5]
print(y)
