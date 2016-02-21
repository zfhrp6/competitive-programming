n,t = list(map(int, input().split(' ')))
tim = []
a = []
b = []
di = []


for i in range(n):
  _a,_b = list(map(int, input().split(' ')))
  tim.append((_a,_b,_b-_a))
  a.append(_a)
  b.append(_b)
  di.append(_b-_a)
suma = sum(a)
sumb = sum(b)
sumdi = sum(di)

if sumb > t:
  print(-1)
elif suma <= t:
  print(0)
else:
  suma_t = suma - t
  sdi = sorted(di)
  # print('sdi',sdi)
  cnt = 0
  for _di in sdi:
    suma_t += _di
    cnt += 1
    # print('_di',_di)
    # print('suma_t',suma_t)
    if suma_t <= 0:
      break
  print(cnt)

