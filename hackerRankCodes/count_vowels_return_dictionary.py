def vowel_count(my_str):
    """
    This function counts the number of vowels in a string and returns a dictionary.
    """
    vowels = 'aeiou'
    my_str = my_str.lower()
    vow_count = {}

    for char in my_str:
        if char in vowels:
            if char in vow_count.keys():
                vow_count[char] = vow_count[char] +1
            else:
                vow_count[char] = 1
    return vow_count

count = vowel_count('ZEROOOO')
print(count)