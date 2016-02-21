spe = 'atcoder'
s, t = input(), input()
f = True
for idx,i in enumerate(s):
  if i!=t[idx]:
    if t[idx] in spe and i=='@':
      pass
    elif i in spe and t[idx]=='@':
      pass
    else:
      f = False
      break
print('You can win' if f else 'You will lose')