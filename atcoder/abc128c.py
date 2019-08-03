N, M = list(map(int, input().split()))
Sw = []
for i in range(M):
    k, *ss = list(map(int, input().split()))
    Sw.append((k, ss))
ps = list(map(int, input().split()))
for idx,p in enumerate(ps):
    Sw[idx] = (Sw[idx][0], Sw[idx][1], p)
# print(Sw)

def is_on(sw_i, strbi, pi):
    # print(sw_i, strbi, pi)
    return len(list(filter(lambda x:x, map(lambda i: bool(int(strbi[i-1])), sw_i[1]))))%2 == pi

cnt = 0

for strb in [str(bin(x))[2:] for x in range(0, 2**N)]:
    if all(map(lambda sw: is_on(sw, strb.zfill(N), sw[2]), Sw)):
        cnt += 1

print(cnt)
