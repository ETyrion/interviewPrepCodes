def perfect_num(num):
    divisor_sum = 0
    n = num
    for i in range(1,num):
        if (num%i ==0):
            divisor_sum = divisor_sum+i

    if (divisor_sum == n):
        print('True')
    else:
        print('False')

perfect_num(28)
