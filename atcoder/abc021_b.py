input()
s=input().split()
input()
s=s+input().split()
# print(s)
# print(list(set(s)))
if len(s)==len(list(set(s))):
  print('YES')
else:
  print('NO')
