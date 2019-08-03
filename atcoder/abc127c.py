N, M = list(map(int, input().split()))
Ls, Rs = [], []
for i in range(M):
    n, m = list(map(int, input().split()))
    Ls.append(n)
    Rs.append(m)

# ll = Ls[0]
# rr  =Rs[0]
# for i in range(M):
#     ll = max(ll, Ls[i])
#     rr = min(rr, Rs[i])
#
# print(rr - ll + 1)
print(max(0, min(Rs) - max(Ls) + 1))

