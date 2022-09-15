list_ip = [9, 8, 7, 6, 4, 2, 1, 3]
arr_len = len(list_ip)

def rotate(arr, n):
    last_ele = arr[-1]
    element_to_be_rotated = last_ele
    print(element_to_be_rotated)
    print(arr)
    #rotated_arr =[]
    arr.insert(0,last_ele)
    arr.pop()
    print(arr)


#list_ip = [9, 8, 7, 6, 4, 2, 1, 3]
rotate(list_ip, arr_len)