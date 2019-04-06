n=int(input())
# ar = [int(input()) for _ in range(n)]
ar = []
cnt = 0
for _ in range(n):
    c = int(input())
    # for l in ar:
    # if c<l and c:
    if any(map(lambda x:c<x, ar)):
        cnt+=1
    ar.append(c)
print(cnt)
