def print2largest(arr, n):
    # code here
    uniq_arr = list(set(arr))
    uniq_arr.sort()

    arr_size = len(uniq_arr)

    if arr_size >=2:
        return uniq_arr[-2]
    else:
        return -1


list_ele = [5,5,6,6,6,6]

ele_size = len(list_ele)

ele = print2largest(list_ele, ele_size)
print(ele)
