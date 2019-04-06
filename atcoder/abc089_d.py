def dist(a, b):
  return abs(a[0] - b[0]) + abs(a[1]- b[1])

H, W, D = map(int, input().split())
matrix = []
dic = {}
for h in range(H):
  line = list(map(int, input().split()))
  matrix.append(line)
  for idx,w in enumerate(line):
    dic[w] = (idx,h)

_ab_cost = {}
def ab_cost(L, R):
  if (L, R) in _ab_cost.keys():
    return _ab_cost[(L,R)]
  _cost = 0
  while L != R:
    _cost += dist(dic[L], dic[L+D])
    _ab_cost[(L, L+D)] = _cost
    L = L+D
  _ab_cost[(L,R)] = _cost
  return _ab_cost[(L,R)]

Q = int(input())
for q in range(Q):
  L, R = map(int, input().split())
  cost = 0
  if L == R:
    print(cost)
    continue
  cost = ab_cost(L, R)
  print(cost)
