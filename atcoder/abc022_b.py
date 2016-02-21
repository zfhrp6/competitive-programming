n = int(input())
s = set({})
cn = 0
for _ in range(n):
  c = input()
  if c in s:
    cn += 1
  s.add(c)
print(cn)
