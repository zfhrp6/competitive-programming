N, K = list(map(int, input().split()))

def needcount(cycoro, K):
    c = 0
    while cycoro * 2 ** c < K:
        c += 1
    return c

ans = 0
for i in range(1, N+1):
    ans += 1/N * (1/2) ** needcount(i, K)
print(ans)
