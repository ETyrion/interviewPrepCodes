#printing a list using for loop

list_1 = [1,2,3,4,5]

for i in list_1:
    print(i)

#print the sum of first 5 natural numbers

print("Printing the sum of first 5 natural numbers")
sum =0

for i in range(1,6):
    print("number is "+str(i))
    sum = sum+i

    print("Sum of first "+str(i)+" numbers is "+str(sum))


#*************************************************

i=1
sum=0

while i<6:
    sum = sum+i
    i = i+1
    print(sum)


#*************************************************

list = ['A', 'B', 'C']

for i in range(len(list)):
    print("Hello")
    print(list[i])

#*************************************************

n=5

def print_pyramid(n):
    for i in range(0, n+1):
        for j in range(1,i+1):
            print(j, end='')
        print()

print_pyramid(5)


