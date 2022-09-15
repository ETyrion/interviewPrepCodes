def is_prime(num):
    flag=0
    if num < 1:
        flag = -1

    if (num>2) and (num%2 == 0):
        flag =-1
    else:
        for i in range(3,num//2):
            if (num%i == 0):
                flag=-1
    return flag

prime_check = is_prime(79)

if (prime_check==-1):
    print('False')
else:
    print('True')


