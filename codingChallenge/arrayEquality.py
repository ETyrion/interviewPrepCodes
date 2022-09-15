A = {1,2,5,4,0}
B = {2,4,0,1,5}


def check(a, b,N):
    list_A = list(a)
    print(list_A)
    list_B = list(b)
    print(list_B)

    #if list_A == list_B:
    for i in range(N):
        print(list_A[i] , list_B[i])
        #if list_A[i] == list_B[i]:
        #    print(1)
    if list_A == list_B:
        print(1)
    else:
        print(0)


check(a= A , b=B, N=5)
