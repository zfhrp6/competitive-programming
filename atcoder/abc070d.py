N = int(input())
d = {}
for _ in range(N):
    a,b,c = list(map(int, input().split()))
    if a>b:
        a,b=b,a
    d['{}_{}'.format(a,b)] = c
dist = {}

