n = int(input())
s = input()
rs = 'bca'*70+'b'
# print(rs)
# print(rs[(len(rs)-1)//2:(len(rs)-1)//2+1])
if n==1:
  print(0 if s=='b' else -1)
elif n==3:
  print(1 if s=='abc' else -1)
elif n==5:
  print(2 if s=='cabca' else -1)
else:
  p = (n-1)//2
  print((n-1)//2 if rs[(len(rs)-1)//2-p:(len(rs)-1)//2+p+1] == s else -1)

