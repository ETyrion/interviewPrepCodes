# a = 1
# b = 2
# n = int(input('Enter the number of terms '))
# print(" ", a, " ", b ," ")
# for i in range(n):
#     c = a+b
#     a=b
#     b=c
#     print(c, " ")

def fibo(n):
    if n<=1:
        return n
    else:
        c= fibo(n-2) + fibo(n-1)
        return c
n = int(input('Enter number of terms: '))

for i in range(n):
    print(fibo(i))

