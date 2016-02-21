a,b,c,d=map(int,input().split())
print('DRAW' if b/a==d/c else 'TAKAHASHI' if b/a>d/c else 'AOKI')
