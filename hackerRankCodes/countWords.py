def count_occurence(count_str):
    occurence_count = {}
    str_list = count_str.split()

    for words in str_list:
        if words in occurence_count:
            occurence_count[words] = occurence_count[words]+1
        else:
            occurence_count[words] = 1
    print(occurence_count)

count_occurence("HELLO THERE HELLO")


















