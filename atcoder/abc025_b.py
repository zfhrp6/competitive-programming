cn,a,b=map(int,input().split())
n = 0
for _ in range(cn):
  dr,ds=input().split()
  ds=int(ds)
  if a<ds<b:
    pass
  elif ds<=a:
    ds = a
  else:
    ds = b
  if dr[0]=='W':
    n -= ds
  else:
    n += ds
print(('' if n==0 else 'West ' if n<0 else 'East ') + '{}'.format(abs(n)))
