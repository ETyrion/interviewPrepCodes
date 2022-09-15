# num = int(input('Enter the number '))
# fact = 1
#
# for i in range(1, num+1):
#     fact = fact*i
#
# print(fact)

def fact(n):
    if n==1:
        return n
    else:
        c = n*fact(n-1)
        return c

number = int(input('Enter the number : '))

print('Factorial is ', fact(number))
