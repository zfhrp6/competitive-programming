s = input()
K = int(input())

def cord(c):
    return ord(c)-97

def cchr(n):
    return chr(n+97)

def smcheck(c, k):
    return 26-cord(c) <= k

def smcnt(c, k):
    return 26-cord(c)

ans = ''
for c in s:
    sc = smcnt(c, K)
    if sc <= K and sc < 26:
        K -= sc
        ans += cchr((cord(c) + sc)%26)
        # print(K,ans)
    else:
        ans += c
if K>26:
    K = K%26
if K>0:
    lc = ans[-1]
    ans = ans[:-1]
    ans += cchr((cord(lc)+K)%26)

print(ans)
