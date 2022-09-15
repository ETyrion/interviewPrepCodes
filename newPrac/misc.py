def preserve_spaces_reversal(str_list):
    list_convert = list(str_list)
    i=0
    j=len(list_convert) -1

    while(i <j):
        if (list_convert[i]==' '):
            i=i+1
            continue
        elif(list_convert[j]==' '):
            j=j-1
            continue
        else:
            list_convert[i], list_convert[j] = (list_convert[j], list_convert[i])
        
            i = i+1
            j = j-1

    print( ' '.join(list_convert))

preserve_spaces_reversal('HE LLO THERE')