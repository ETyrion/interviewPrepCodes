A = [1, 2, 4, 5, 7]
B = [5, 6, 3, 4, 8]
X=9

N = len(A)
M = len(B)

def pairs_with_sum(a,b,n,m, X):
    res= []
    for i in range(n):
        for j in range(m):
            if (a[i] + b[j] == X):
                res.append((i,j))
    print(res)

pairs_with_sum(A,B,N, M, X)

# def findPairs(lst, K):
#     res = []
#     while lst:
#         num = lst.pop()
#         diff = K - num
#         if diff in lst:
#             res.append((diff, num))
#
#     #res.reverse()
#     return res
#
#
# # Driver code
# lst = [1, 5, 3, 7, 9]
# K = 12
# print(findPairs(lst, K))