l,h = map(int,input().split())
n = int(input())
for _ in range(n):
  i=int(input())
  print(0 if l<=i<=h else l-i if i<l else '-1')
