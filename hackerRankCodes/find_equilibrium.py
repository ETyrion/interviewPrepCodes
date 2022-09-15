def equilibrium_index(num_list):
    for x in range(0, len(num_list)):
        l_sum = sum(num_list[:x])
        r_sum = sum(num_list[x+1:])
        if sum(num_list[:x]) == sum(num_list[x+1:]):
            return x
    return False
nums = [2, 3, 10, 5]
print(equilibrium_index(nums))