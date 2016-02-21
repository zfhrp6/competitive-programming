a = int(input())
b  =int(input())
c = int(input())

if   a<b<c:
    aa = 3
    bb = 2
    cc = 1
elif a<c<b:
    aa = 3
    bb = 1
    cc = 2
elif b<a<c:
    aa  =2
    bb = 3
    cc=  1
elif b<c<a:
    aa = 1
    bb  =3
    cc = 2
elif c<a<b:
    aa = 2
    bb = 1
    cc = 3
else:
    aa = 1
    bb  =2
    cc=  3

print(aa)
print(bb)
print(cc)