N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

fixed_peek_t = {}
unfixed_peek_t = {}
fixed_peek_a = {}
unfixed_peek_a = {}

lp = 0
for idx, height in enumerate(T):
    if lp < height:
        fixed_peek_t[idx] = height
    elif idx not in fixed_peek_t:
        unfixed_peek_t[idx] = height
    lp = height

lp = 0
for _idx, height in enumerate(reversed(A)):
    idx = N-1 - _idx
    if lp < height:
        fixed_peek_a[idx] = height
    elif idx not in fixed_peek_a:
        unfixed_peek_a[idx] = height
    lp = height

# print(unfixed_peek_t)
# print(fixed_peek_t)
# print(unfixed_peek_a)
# print(fixed_peek_a)

if max(A) != max(T):
    print(0)
else:
    failflag = 0
    for k,v in fixed_peek_t.items():
        if k not in fixed_peek_a:
            continue
        if v != fixed_peek_a[k]:
            failflag = 1
            break
        if k in unfixed_peek_a and v > unfixed_peek_a[k]:
            failflag = 1
            break
    for k,v in unfixed_peek_t.items():
        if k not in fixed_peek_a:
            continue
        if v < fixed_peek_a[k]:
            failflag = 1
            break
    if failflag == 0:
        cnt = 1
        for k,v in unfixed_peek_t.items():
            if k not in unfixed_peek_a:
                continue
            cnt *= min(v, unfixed_peek_a[k])
            cnt %= 10**9 + 7

        print(cnt)
    else:
        print(0)
