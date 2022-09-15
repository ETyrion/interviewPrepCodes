def rev_with_spaces(str_ip):
    str_to_rev = list(str_ip)
    i =0
    j = len(str_to_rev)-1

    while (i < j):
        if (str_to_rev[i] == ' '):
            i = i+1
            continue
        elif (str_to_rev[j] ==' '):
            j = j-1
        else:
            str_to_rev[i], str_to_rev[j] = str_to_rev[j], str_to_rev[i]
            i = i+1
            j = j-1
    return (' '.join(str_to_rev))

str_to_reverse = 'I love  chocolate chip cookie'

print(rev_with_spaces(str_to_reverse))

