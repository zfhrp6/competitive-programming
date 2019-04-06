N = int(input())
As = map(int, input().split())
cnt = {}
for a in As:
    if a in cnt:
        cnt[a] += 1
    else:
        cnt[a] = 1
ret = 0
for i in set(cnt.keys()):
    if i < cnt[i]:
        ret += cnt[i] - i
    elif cnt[i] < i:
        ret += cnt[i]
print(ret)
