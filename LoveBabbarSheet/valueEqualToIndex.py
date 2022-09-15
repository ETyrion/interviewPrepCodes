def valueEqualToIndex(arr, n):
    # code here
    res=[]
    for i in range(0, n):
        if arr[i] == i+1:
            res.append(i+1)
    print(res)

list_arr = [5,2,1,4,3,6]
n = len(list_arr)

valueEqualToIndex(list_arr, n)
