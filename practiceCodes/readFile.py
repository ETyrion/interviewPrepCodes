f = open('test.txt')
content = f.read()
print(content)
f.close()

with open('test.txt') as file:
    print(file.read())
    print(file.closed)