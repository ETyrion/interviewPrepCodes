get_quotes = open('quotes.txt')

get_quotes_list = get_quotes.read().splitlines()
print(get_quotes_list)

get_quotes.close()