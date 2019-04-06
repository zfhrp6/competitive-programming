from math import gcd

N, X = map(int, input().split())
xs = list(map(int, input().split()))
xs.append(X)
xs = sorted(xs)
m = 999999999999999999
diffs = []
for idx,e in enumerate(xs):
  if idx==0:
    continue
  diff = abs(e - xs[idx-1])
  diffs.append(diff)
diffs = sorted(diffs)
for idx,dif in enumerate(diffs):
  if idx == 0:
    continue
  if gcd(diffs[idx], diffs[idx-1]) < m:
    m = gcd(diffs[idx], diffs[idx-1])
if len(diffs) == 1:
  m = diffs[0]
print(m)
