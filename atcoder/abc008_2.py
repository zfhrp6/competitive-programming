n = int(input())
d = {}
for _ in range(n):
  s = input()
  if s in d:
    d[s]+=1
  else:
    d[s] = 1
ma = (-1,-1)
for kv in d.items():
  if kv[1] > ma[1]:
    ma = kv
print(ma[0])