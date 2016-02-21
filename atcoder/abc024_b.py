n,t=tuple(map(int, input().split()))

s = 0
la=-1111111111111
for _ in range(n):
  a = int(input())
  s += t
  s -= (a<la+t)*(la+t-a)
  la = a
print(s)
