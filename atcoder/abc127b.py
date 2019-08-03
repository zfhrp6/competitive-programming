def next(r,d,x):
  return r*x - d

r,d,x = list(map(int, input().split()))


for i in range(10):
  x = next(r,d,x)
  print(x)
