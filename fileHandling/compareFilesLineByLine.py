file1 = open('Zoo_file_1.txt')
file2 = open('Zoo_file_2.txt')

file1_contents = file1.read().splitlines()

file2_contents = file2.read().splitlines()

zip_files = list(zip(file1_contents, file2_contents))

print(zip_files)

i=0

for item in zip_files:
    print(item)
    i = i+1
    if item[0] != item[1]:
        print(item[0], item[1])

