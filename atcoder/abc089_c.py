import itertools as it

def c(n,k):
  if k>n:
    return 0
  ret = 1
  for i in range(n, n-k, -1):
    ret *= i
  for i in range(k, 1, -1):
    ret /= i
  return ret


n = int(input())
dic = {'M':0, 'A':0, 'R':0, 'C':0, 'H':0}
for person in range(n):
  name = input()
  if name[0] in 'MARCH':
    dic[name[0]] += 1

answer = 0
for a,b,c in it.combinations('MARCH', 3):
  answer += dic[a] * dic[b] * dic[c]
print(answer)
