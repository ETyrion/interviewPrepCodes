arr = [1,2,3,4,5]
k = 5
arr_len = len(arr)

def binary_search(arr, n):
    start = 0
    end = arr_len
    #mid = (start+end)//2
    while (start < arr_len):
        mid = (start+end)//2
        if arr[mid] > n:
            end = mid-1
        elif n > arr[mid]:
            start = start+1
        else:
            return mid-1

pos = binary_search(arr, k)
print(pos)