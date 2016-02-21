n = int(input())

a = list(map(int, input().split(' ')))
# for _ in range(n):
  # a.append(int(input()))

ret = 0

for i in range(n):
  ret += a[i]*(2**(n-1-i))

print(ret)

