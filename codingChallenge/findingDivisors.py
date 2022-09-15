num = int(input('Provide the number: '))
div_list=[]

#number = int(num)
for divisor in range(1, num):
    if num%divisor ==0:
        div_list.append(divisor)

print(div_list)

x = int(input("Enter a number: "))
all_divisors = list()
for i in range(2, x//2+1):
    if x % i == 0:
        all_divisors.append(i)

print(all_divisors)