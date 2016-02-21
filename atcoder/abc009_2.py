n = int(input())
m1,m2 = 0,0
for _ in range(n):
  i = int(input())
  if m1>i:
    m2 = max(m2,i)
  elif m1==i:
    pass
  else:
    m1,m2 = i,m1
print(m2)