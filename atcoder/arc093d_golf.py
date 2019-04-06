p,h,l,s,w,b,r=print,80,40,list,'.','#',range
W,B=map(int,input().split())
m=s(map(s,zip(*[iter(w*h*l+b*h*l)]*h)))
for i in r(B-1):m[i//l*2][i%l*2]=b
for i in r(W-1):m[79-i//l*2][79-i%l*2]=w
p(h,h)
[p(''.join(l)) for l in m]
