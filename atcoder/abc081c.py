N, K = list(map(int, input().split()))
As = input().split()
dic = {}
for c in As:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1

values = list(sorted(dic.values()))

if len(values) <= K:
    print(0)
else:
    print(sum(values[:len(values)-K]))


