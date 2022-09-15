n = int(input('Please provide the number: '))

length = len(str(n))
dig_sum=0

while n!=0:
    n = n%10
    dig_sum = dig_sum+ pow(n,length)

if dig_sum == n:
    print('Yes')
else:
    print('No')