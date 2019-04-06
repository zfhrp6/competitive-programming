N, L = list(map(int, input().split()))
As = list(map(int, input().split()))

sumL = sum(As)

l,r = 0, N-1
ans = []
cnt = 0

center = -1
for i in range(N-1):
    if As[i]+As[i+1]>=L:
        center = i+1
        break
if center < 0:
    print('Impossible')
else:
    print('Possible')
    for i in range(center-1):
        print(i+1)
    for i in range(N-1, center, -1):
        print(i)
    print(center)
# while sumL>=L and cnt < N-1:
#     # print(l,r,As[l],As[r])
#     if As[l] < As[r]:
#         # print('l<')
#         l += 1
#         sumL -= As[l]
#         ans.append(l)
#         cnt += 1
#     else:
#         # print('r<')
#         r -= 1
#         sumL -= As[r+1]
#         ans.append(r+1)
#         cnt += 1
#     # print('suml',sumL)
# if cnt==N-1:
#     print('Possible')
#     for _a in ans:
#         print(_a)
# else:
#     print('Impossible')
