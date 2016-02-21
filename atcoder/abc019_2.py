ret = ''
lc = ''
cn = 0
s = input()
for c in s:
  # print(c,end='')
  if lc==c:
    cn+=1
  elif lc!='':
    ret=ret+'{}{}'.format(lc,cn+1)
    cn=0
  lc=c
ret=ret+'{}{}'.format(lc,cn+1)
print(ret)
