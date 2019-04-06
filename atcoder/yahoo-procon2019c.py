K, A, B = list(map(int, input().split()))

def calc(k, a, b, now):
  if b-a<2:
    return now + k
  while k>0:
    if k==1:
      now += 1
      k-=1
      continue
    if k==0:
      break
    if now<a:
      if (a-now) < k:
        now += a-now
        k -= a-now
        continue
      now += k
      k -= k
      continue
    if k>=2:
      now = now - a + b
      k -= 2
      continue
    k -= 1
    now += 1
  return now

def c(k, a, b, now):
  if b-a<=2:
    print(1)
    return now+k
  if a-now>k:
    print(2)
    return now+k
  if now < a:
    print(3)
    return c(k-a+now, a, b, b)
  if now >= a:
    print(4)
    if k//2 > now//a:
      return c(k-now//a, a, b, now+(b-a)*(now//a))
    return c(k-k//2, a, b, now+(b-a)*(k//2))
  return c(k-1, a, b, now+1)

print(c(K, A, B, 1))
