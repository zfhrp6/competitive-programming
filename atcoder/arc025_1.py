ds = list(map(int,input().split(' ')))
js = list(map(int,input().split(' ')))

ret = 0
for i in range(len(ds)):
    ret += max(ds[i],js[i])

print(ret)
