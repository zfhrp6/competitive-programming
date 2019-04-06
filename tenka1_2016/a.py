def in():
    return input().split()

def iin():
    return list(map(int, input().split()))

N, M = iin()
P = [0]
for i in range(N-1):
    P.append(int(input()))
B = []
C = []
for i in range(M):
    tmp = iin()
    B.append(tmp[0])
    C.append(tmp[1])

ans = 0
for idx,i in enumerate(C):

