# # def fact(n):
# #     if n==1:
# #         return n
# #     else:
# #         fact_result = n*fact(n-1)
# #         return fact_result
# #
# # print(fact(10))
#
# def fibo(n):
#     if n<=1:
#         return n
#     c = fibo(n-2)+fibo(n-1)
#     return c
#
# terms = int(input('Enter number of terms: '))
#
# for i in range(terms):
#     print(fibo(i))
n = int(161)
num=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("The reverse of the number:",rev)

if rev==num:
    print('Number is palindrome')
else:
    print('Not')

