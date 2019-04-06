n,m = list(map(int, input().split()))
d = {}
for i in range(1,n+1):
    d[i] = 0
for _ in range(m):
    for i in map(int, input().split()):
        d[i] += 1
for i in range(1,n+1):
    print(d[i])

