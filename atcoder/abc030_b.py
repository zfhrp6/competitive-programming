n,m = map(int,input().split())
md = m*90/15
nd = (n*30+m/2)%360
print(min(360-max(md-nd,nd-md),max(md-nd,nd-md)))
