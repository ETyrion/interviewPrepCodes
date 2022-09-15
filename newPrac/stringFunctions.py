str = "123 ABC D456"
str2 = str[::-1]
print(str2)

#slicing of strings

slice_str = str[-1:1:-1]
print(slice_str)

name = "Abhishek"

name2 = name*5

print(name2)

movie = 'Star Wars The Jedi'

sliced_movie = movie[:-8]

print(sliced_movie)

print(sliced_movie[::-1])

chunk_in_rev = movie[:-3]

print(chunk_in_rev)

#check if a string is palindrome

str = "Exact"
print(str)
revstr = str[::-1]
print(revstr)
if revstr == str:
    print('palindrome')

else:
    print('Not a palindrome')