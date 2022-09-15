def file_dict_with_name_and_len(file_name):
    with open(file_name) as f:
        file_contents = f.read().splitlines()
        #print(file_contents)
        file_dict = {}
        for val in file_contents:
            #file_value = val
            #print(file_value)
            file_dict[val] = len(val)

        print(file_dict)

file_dict_with_name_and_len('Zoo_file_1.txt')

#file_dict_with_name_and_len('count_lengths.txt')


