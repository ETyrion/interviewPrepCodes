def count_char(my_str):
    char_count = {}

    for char in my_str:
        if char in char_count.keys():
            char_count[char] = char_count[char] +1
        else:
            char_count[char] = 1
    return char_count
print(count_char('AWWWWESOMEEEEAAA'))