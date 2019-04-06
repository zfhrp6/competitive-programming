n=int(input())
ar = [int(input()) for _ in range(n)]
# ar = []
cnt = 0
for idxi in range(1,n+1):
    if idxi!=ar[idxi-1]:
        ar.remove(idxi)
        ar.insert(idxi-1,idxi)
        cnt += 1
print(cnt)

# def ld(s1, s2):
#     if s1==s2:
#         return 0
#     elif s1=='' or s2=='':
#         return max(map(len, [s1,s2]))
#     else:

