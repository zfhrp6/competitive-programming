su = 0
m = [0,'name']
n = int(input())
for _ in range(n):
  s,p = input().split()
  p=int(p)
  if m[0] < p:
    m[0]=p
    m[1]=s
  su+=p
print('atcoder' if not m[0]>su/2 else m[1])
