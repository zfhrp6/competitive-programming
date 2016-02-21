m=10**9+7;v=lambda x:pow(x,m-2,m);a=1;n,k=int(input()),int(input());n=n+k-1
for i in range(k):
 a=(a*(n-i)*v(i+1))%m
print(a)
