H, W = list(map(int, input().split()))

objet = []
for row in range(H):
    objet.append(list(input()))

a = ''
b = ''
c = ''

for _r in range(H):
    for _c in range(W):
        if _c == 0:
            a += objet[_r][_c]
        elif _c == 1:
            b += objet[_r][_c]
        elif _c == 2:
            c += objet[_r][_c]
        else:
            pass

def cost(sele, surround):
    cnt = 0
    for idx,c in enumerate(sele):
        for seq in surround:
            if c == seq[idx]:
                cnt += 1
    return cnt

def next_cost(sele, surround):
    cnt = 0
    for idx,c in enumerate(sele):
        if idx == len(sele)-2:
            break
        for seq in surround:
            if c == seq[idx+1]:
                cnt += 1
    return cnt


def main(a,b,c,H,W,objet):
    if W>3:
        print(-1)
        return
    ans = 0
    for _ in range(H*W):
        cost_a = cost(a, (b,))
        ncost_a = next_cost(a, (b,))
        cost_b = cost(b, (a,c))
        ncost_b = next_cost(b, (a,c))
        cost_c = cost(c, (b,))
        ncost_c = next_cost(c, (b,))
        print(cost_a, cost_b, cost_c)
        mincost = min(cost_a, cost_b, cost_c)
        min_ncost = min(ncost_a, ncost_b, ncost_c)
        if cost_a == mincost and ncost_a == min_ncost:
            a = 'A' + a[:-1]
        elif cost_b == mincost and ncost_b == min_ncost:
            b = 'B' + b[:-1]
        elif cost_c == mincost and ncost_c == min_ncost:
            c = 'C' + c[:-1]
        ans += mincost
        print(a,b,c)
    print(ans)

if __name__ == '__main__':
    main(a,b,c,H,W,objet)
