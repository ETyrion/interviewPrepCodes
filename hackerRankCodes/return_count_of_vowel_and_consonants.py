def counter(my_str):
    my_str = my_str.lower()
    #vow_and_cons_count = {'v':0, 'c':0}
    alpha_count = [0,0]
    vowels = 'aeiou'

    for char in my_str:
        if char in vowels:
            #vow_and_cons_count['v'] = vow_and_cons_count['v']+1
            alpha_count[0] = alpha_count[0]+1
        else:
            #vow_and_cons_count['c'] = vow_and_cons_count['c']+1
            alpha_count[1] = alpha_count[1] + 1
    #return vow_and_cons_count
    return tuple(alpha_count)
print(counter('AWESOME'))