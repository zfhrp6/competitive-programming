n = int(input())
As = list(map(int, input().split()))

As = sorted(As,reverse=True)

def d(*arg):
    # print(' '.join(map(str,arg)))
    pass

last = 0
ret = 0
leng = len(As)
for idx,a in enumerate(As):
    if 2*a < last:
        if 2*sum(As[idx:])>=last:
            ret += 1
            d('\t',last,ret,leng,idx,a)
        else:
            d('\t',last,ret,leng,idx,a)
            break
            # pass
    else:
        d('\t',last,ret,leng,idx,a)
        ret += 1
    d('\t\t',last,ret,leng,idx,a)
    last = a
print(ret)
