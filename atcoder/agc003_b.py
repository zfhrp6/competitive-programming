N = int(input())
As = []
for _ in range(N):
    As.append(int(input()))

ans = 0
for idx,a in enumerate(As):
    if idx!=len(As)-1:
        tmp = As[idx]
        ans += tmp//2
        As[idx] = 1 * As[idx]%2

        tmp = min(As[idx], As[idx+1])
        # print('\t', tmp)
        ans += tmp
        As[idx] -= tmp
        As[idx+1] -= tmp
    else:
        tmp = As[idx]
        ans += tmp//2
        As[idx] = 1 * As[idx]%2
    # print(ans,As)

As = list(reversed(As))
for idx,a in enumerate(As):
    if idx!=len(As)-1:
        tmp = As[idx]
        ans += tmp//2
        As[idx] = 1 * As[idx]%2

        tmp = min(As[idx], As[idx+1])
        # print('\t', tmp)
        ans += tmp
        As[idx] -= tmp
        As[idx+1] -= tmp
    else:
        tmp = As[idx]
        ans += tmp//2
        As[idx] = 1 * As[idx]%2
    # print(ans,As)
# print('hhh')
print(ans)
