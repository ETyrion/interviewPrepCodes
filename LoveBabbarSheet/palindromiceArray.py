def palindromic_array_check(arr, n):
    is_palindrome = []
    for i in range(n):
        print(arr[i])
        num = arr[i]
        rev =0
        tem=num

        while num > 0:
            rem = num % 10
            rev = rev*10 + rem
            num = num//10
        if (tem != rev):
            return 0

    return 1

#list_ip = [111, 2221, 333, 444, 555, 555]
list_ip = [121, 131, 303]

len_ip = len(list_ip)
is_palindromic = palindromic_array_check(list_ip,len_ip)

if is_palindromic ==0:
    print('False')
else:
    print('True')
