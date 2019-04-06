n, c, k = list(map(int, input().split()))
ts = []
for i in range(n):
    ts.append(int(input()))
ts = sorted(ts)
cnt = 0
fst = 0
ret = 1
for p in ts:
    if fst==0:
        fst = p
        cnt += 1
    elif p-fst > k or cnt >= c:
        ret += 1
        cnt = 1
        fst = p
    else:
        cnt += 1
    # print("\t", cnt ,fst, ret, p)
print(ret)


