# Given: A list of integers and the resulting sum to find
# To find: Indices of all the pairs resulting that sum

# def printPairs(arr, n, sum):
#     for i in range(0, n):
#         for j in range(i+1, n):
#             if arr[i]+arr[j] == sum:
#                 print('Indices are ', i, ' and ', j)
#
# num_list = [12, 21, 33, 43, 11, 44]
# n = len(num_list)
# sum=55
#
# printPairs(num_list, n, sum)
#
# def printPairs(arr, sum):
#     i=0
#     j = len(arr)-1
#
#     while (i < j):
#         if ((arr[i] + arr[j]) == sum):
#             print(f'{i} , {j}')
#         if (((arr[i] + arr[j])) > sum):
#             j = j-1
#         else:
#             i = i+1
#
# num_list = [30, 10, 45, 50, 25, 5, 45]
# sorted_num_list = num_list.sort()
# sum = 55
# printPairs(num_list, 55)

# def return_indices(arr_list, n, sum):
#     high = n - 1
#     low = 0
#
#     while(low < high):
#         if ((arr_list[low] + arr_list[high]) == sum):
#             print(f'{low} , {high}')
#
#         if ((arr_list[low] + arr_list[high]) > sum):
#             high = high - 1
#         else:
#             low = low + 1
#
# array_list = [30, 10, 45, 50, 25, 5, 45]
# array_list.sort()
# print(array_list)
# sum = 55
# len = len(array_list)
# return_indices(array_list, len, sum)

def return_indices(input_list, n, sum):
    i=0
    j=n-1
    index= []
    while i <j:
        if ((input_list[i] + input_list[j]) ==sum):
            print(f'{i} , {j}')
        if ((input_list[i] + input_list[j]) > sum):
            j = j-1
        else:
            i = i+1

ip_list = [50, 45,80, 55, 50, 40, 60]
ip_list.sort()
print(ip_list)
n = len(ip_list)
sum = 100

return_indices(ip_list, n, sum)

































































