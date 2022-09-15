def count_lines(file_name):
    with open(file_name, 'r') as f:

        file_contents = f.read().splitlines()
        print(len(file_contents))

count_lines('quotes.txt')