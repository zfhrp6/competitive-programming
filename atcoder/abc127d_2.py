N, M  = map(int,input().split())
As = sorted(list(map(int,input().split())))
querys = {}
for i in range(M):
    b, c = map(int,input().split())
    querys[c] = querys.get(c, 0) + b

keys = list(sorted(querys.keys(), reverse=True))
ichi = 0
for i in range(N):
    try:
        if keys[ichi] > As[i]:
            As[i] = keys[ichi]
            querys[keys[ichi]] -= 1
        else:
            break
        if querys[keys[ichi]] == 0:
            ichi += 1
    except:
        pass
print(sum(As))
