n=int(input())
ar = [int(input()) for _ in range(n)]
cor = [x for x in range(1,n+1)]
cnt = 0
c_idx,a_idx = 0,0
while c_idx<n and a_idx<n:
    if cor[c_idx]<ar[a_idx] and ar[a_idx]<=a_idx:
        print('\t',cor[c_idx],ar[a_idx])
        cnt+=1
        a_idx+=1
    else:
        a_idx+=1
        c_idx+=1
print(cnt)
