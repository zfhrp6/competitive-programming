W, H = list(map(int, input().split()))
ps, qs = [], []
for _ in range(W):
    ps.append(int(input()))
for _ in range(H):
    qs.append(int(input()))

already = {}
already.add('0,0')

