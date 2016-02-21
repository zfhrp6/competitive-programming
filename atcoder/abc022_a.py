n,s,t = list(map(int, input().split()))
sw = int(input())
ret = 0
if s<= sw <=t:
  ret += 1
for _ in range(n-1):
  sw += int(input())
  if s <= sw <= t:
    ret += 1
print(ret)
