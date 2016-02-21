n=int(input())
rounds=lambda x:x-x%5
rounde=lambda x:x+(5-x%5 if x%5 else 0)
prt=lambda s,e:print(('{}-{}\n'.format(str(s).zfill(4),str(e).zfill(4))) if s>=0 and e>=0 else '', end='')
ls,le=-1,-1
sss=[]
for _ in range(n):
    s,e=map(int,input().split('-'))
    sss.append((rounds(s),rounde(e)))
sss=sorted(list(set(sss)))
for idx,i in enumerate(sss):
    s,e=i[0],i[1]
    if s<=le or (s-le==40 and le%100==60):
        le=max(e,le)
        if (le%100==60):
            le+=40
    elif ls<=s and e<=le:
        pass
    else:
        prt(ls, le)
        ls,le=s,e
        if (le%100==60):
            le+=40
prt(ls,le)
