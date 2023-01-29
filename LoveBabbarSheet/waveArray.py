def waveArray(ip_sorted_list, arr_size):
    temp = ip_sorted_list[0]

    for i in range(0, arr_size-1, 2):
        temp = ip_sorted_list[i]
        ip_sorted_list[i] = ip_sorted_list[i+1]
        ip_sorted_list[i+1] = temp


    print(ip_sorted_list)

ip_list = [1,2,3,4,5,6]

waveArray(ip_list, 6)
