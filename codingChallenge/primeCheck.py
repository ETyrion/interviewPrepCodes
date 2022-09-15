n = int(input('Provide a nmber: '))
flag=0

if n<2:
    flag=1
elif (n > 2) and (n%2==0):
    flag=1
elif n>7:
    for i in range (3,n//2):
        if n%i ==0:
            flag=1

if flag == 1:
    print('Not a prime number')
else:
    print('A prime number')