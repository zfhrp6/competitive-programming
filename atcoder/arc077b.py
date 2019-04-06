n = int(input())
seq = input().split()
lc = 'a'
already = []
for idx,c in enumerate(seq):
    if c in already:
        break
    already.append(c)
    lc = c

left = seq.index(c)
right = list(reversed(seq)).index(c)
middle = n-left-right-2
# print(left,middle,right,lc)
# print(seq)
NUM = 10**9+7

# def f(n):
#     if n<=1:
#         return 1
#     else:
#         return n*f(n-1)
#
from math import factorial
def f(n,k):
    if n<k:
        return 1
    else:
        return n*f(n-1,k)


def c(n,k):
    if k == 1:
        return n
    if k == n:
        return 1
    # return f(n)//(f(k) * f(n-k))
    return f(n,max(k,n-k)+1)//f(min(k,n-k),1)

# from itertools import combinations as combi
# def c(n,k):
#     return len(list(combi(range(n),k)))

def calc(n,k):
    if k == 1:
        return n-1
    if k == n:
        return 1
    # if k == n-1:
    #     return c(n,k) - 1
    # if k == 2:
    #     return c(n,k) - lidx - (n-ridx)
    # if k == 3:
    #     return c(n,k) - c(lidx,1) * c(n-ridx,1)
    # if k == 4:
    #     return c(n,k) - c(lidx,1) * c(n-ridx,2) - c(lidx,2) * c(n-ridx,1)
    if k-1 > left+right:
        return c(n,k)
    else:
        return c(n,k) - c(left+right, k-1)


for k in range(1,n+1 +1):
    print(int(calc(n+1,k))%NUM)
