N, x = list(map(int, input().split()))
As = list(map(int, input().split()))
di = {}
ans = 0
for i in range(1, N+1):
    tmp = 10**10
    for j in range(1, N+1):
        if i==j:
            tmp = min(tmp, As[i-1])
        else:
            tmp = min(tmp, (i-j)*x+As[j-1] if j<i else (N+i-j)*x+As[j-1])
    # di[i] = tmp
    ans += tmp
print(ans)
