n=int(input())
a = tuple(map(int, input().split()))
numBridges=0
if sum(a)%n!=0:
  print(-1)
else:
  av = sum(a)//n
  c,d=0,0
  tm = 0
  for ai in a:
    c+=1
    tm += ai
    if tm/c==av:
      numBridges+=(c-1)
      c,tm=0,0
  print(numBridges)
