n = int(input())
As = [int(input()) for _ in range(n)]
sAs = sorted(list(set(As)))
dAs = {}
for idx, val in enumerate(sAs):
    dAs[val] = idx
for idx,val in enumerate(As):
    print(dAs[val])

