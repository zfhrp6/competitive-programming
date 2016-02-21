a1,a2,a3=0,0,1
n = int(input())
M = 10007
if n<3:
  print(0)
else:
  for i in range(n-3):
    a1,a2,a3 = a2,a3,(a1+a2+a3)%10007
  print(a3%M)
