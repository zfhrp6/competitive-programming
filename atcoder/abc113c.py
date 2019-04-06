N, M = list(map(int, input().split()))

PYs = {}

py2nummap = {}
py2 = []
for _ in range(M):
    p, y = list(map(int, input().split()))
    if p not in PYs:
        PYs[p] = []
    PYs[p].append(y)
    py2nummap[(p,y)] = ''
    py2.append((p,y))

for p in sorted(PYs.keys()):
    str_p = '{}'.format(p).zfill(6)
    for idx, c in enumerate(sorted(PYs[p])):
        py2nummap[(p,c)] = (str_p + '{}'.format(idx + 1).zfill(6))


for y in py2:
    # print(y)
    print(py2nummap[y])
# print(py2nummap)
# print(PYs)
