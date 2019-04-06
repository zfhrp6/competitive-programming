R, B = map(int, input().split())
x, y = map(int, input().split())

def maxx(r, b):
    recnt = b if r//x > b else r//x
    return (recnt, r-recnt*x, b-recnt)

def maxy(r, b):
    recnt = r if b//y > r else b//y
    return (recnt, r-recnt, b-recnt*y)

cnt = 0
# while R>x or B>y:
#     if R>x:
#         ccnt, R, B = maxx(R, B)
#         cnt += ccnt
#     elif B>y:
#         ccnt, R, B = maxy(R, B)
#         cnt += ccnt


while 1:
    if (R<x and B<y) or R<1 or B<1:
        break
    if R>=x+1 and B>=y+1:
        tmp = min(R//(x+1), B//(y+1))
        R -= (x+1)*tmp
        B -= (y+1)*tmp
        cnt += 2*tmp
    if R>=x and B>=1:
        # tmp = R//x
        R -= x
        B -= 1
        cnt += 1
    if B>=y and R>=1:
        # tmp = B//y
        R -= 1
        B -= y
        cnt += 1

print(cnt)

