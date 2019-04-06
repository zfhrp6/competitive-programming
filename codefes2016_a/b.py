N = int(input())
As = list(map(int, input().split()))
As.insert(0,-1)
cnt = 0
for i in range(N+1):
    j = As[i]
    if j <= i:
        continue
    if As[j] == i:
        cnt += 1
print(cnt)
