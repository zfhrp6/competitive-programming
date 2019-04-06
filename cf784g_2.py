exp = input()
ans = str(eval(exp))

l=len(ans)
print('>'*l+'++++++++')
print('[', end='')
for i in range(l):
    print('<++++++', end='')
print('>'*l+'-]')
print('<'*l)

num = 48
num = 0
for c in ans:
    print('+'*(num+int(c))+'.>')
# print('+'*ans+'.')
