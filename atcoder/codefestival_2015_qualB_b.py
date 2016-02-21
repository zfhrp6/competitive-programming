n,m = list(map(int, input().split(' ')))
ans_d = {}

ans = input().split(' ')
for _a in ans:
    try:
        ans_d[_a] += 1
    except:
        ans_d[_a] = 1

mm = max(ans_d.values())
if n/2 < mm:
    for k in ans_d.keys():
        if ans_d[k] == mm:
            print(k)
            break
else:
    print('?')

