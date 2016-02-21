m = int(input())
# m = 200
if m<100:
  print('00')
elif m<=5000:
  print('{}'.format(m//100).zfill(2))
elif 6000<=m<=30000:
  print('{}'.format(m//1000 + 50))
elif 35000<=m<=70000:
  print('{}'.format((m//1000-30)//5+80))
else:
  print('{}'.format(89))

