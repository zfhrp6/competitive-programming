def bigger(a, b):
    return a[0] > b[0] and a[1] > b[1]


N = int(input())
ab = []
cd = []
for i in range(N):
    ab.append(list(map(int, input().split())))
for i in range(N):
    cd.append(list(map(int, input().split())))

ab = sorted(ab, key=lambda x: (-x[1], -x[0]))
cd = sorted(cd, key=lambda x: (x[0], x[1]))

ret = 0
ab_used, cd_used = [], []
for c in cd:
    for a in ab:
        if a in ab_used:
            continue
        if c in cd_used:
            break
        if bigger(c, a):
            ab_used.append(a)
            cd_used.append(c)
            ret += 1
            break

print(ret)
