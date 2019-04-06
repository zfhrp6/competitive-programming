s = input()
cs = 'CODEFESTIVAL2016'
cnt = 0

for i in range(len(cs)):
    if s[i]==cs[i]:
        continue
    else:
        cnt += 1
print(cnt)
