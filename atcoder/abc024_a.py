a,b,c,k = tuple(map(int,input().split()))
s,t = tuple(map(int,input().split()))
print(a*s+b*t-((s+t)>=k)*(s+t)*c)
