S=input()

def isunbalance(s):
    l = len(s)
    for c in s:
        if s.count(c)>l/2:
            return True
    return False

ans = (-1, -1)
for s in range(len(S)):
    for ln in range(3, min(len(S)-s,17)):
        # print(S[s:s+ln])
        if isunbalance(S[s:s+ln]):
            ans = (s, s+ln-1)
            break
print(ans[0], ans[1])

