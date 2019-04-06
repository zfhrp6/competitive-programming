n,K = list(map(int, input().split()))
seq = []
d = {}
for _ in range(n):
    a,b = list(map(int, input().split()))
    if a in d.keys():
        d[a] += b
    else:
        d[a] = b
c = 0
for k in sorted(d.keys()):
    ans = k
    # print(ans,k,c)
    c += d[k]
    if c >= K:
        ans = k
        break
print(ans)
