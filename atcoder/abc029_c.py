import itertools

n = int(input())

ls = []
for i in range(n):
  ls.append(['a','b','c'])

for i in itertools.product(*ls):
  print(''.join(i))
