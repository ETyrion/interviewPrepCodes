def readFromEnd(file_name, n):
    with open(file_name, 'r') as f:
        tail_file = f.read().splitlines()
        file_len = len(tail_file)
        print(file_len)
        last_three_lines = tail_file[-n:]
        print(tail_file)
        print(last_three_lines)

#ip_file = 'quotes.txt'

readFromEnd('quotes.txt', 5)

fruit_list = ['Apple', 'mango', 'Guava', 'banana', 'pear', 'pineapple']

end_fruit_list = fruit_list[-2:]
print(end_fruit_list)