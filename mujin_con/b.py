l = list(map(int, input().split()))
sl = sum(l)
ml = max(l)
pi = 3.1415926535897932
if ml > sl - ml:
    s = pi*(sl**2 - (2*ml-sl)**2)
else:
    s = pi*sl**2
print(s)
