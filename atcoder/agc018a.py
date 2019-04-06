N, K = list(map(int, input().split()))
As = list(map(int, input().split()))

def calc(seq, target):
    from math import gcd
    if target in seq:
        return 'POSSIBLE'
    if max(seq) < target:
        return 'IMPOSSIBLE'
    dif = []
    target_diff = []
    seq = list(sorted(seq))
    for idx,s in enumerate(seq):
        if target < s:
            target_diff.append(s - target)
        if idx==0:
            continue
        d = gcd(s,seq[idx-1])
        if d == 1:
            return 'POSSIBLE'
        dif.append(d)
    dif = list(sorted(list(set(dif))))
    for d in dif:
        for td in target_diff:
            if td%d == 0:
                return 'POSSIBLE'
    return 'IMPOSSIBLE'

print(calc(As, K))
