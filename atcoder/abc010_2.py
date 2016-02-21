input()
n = map(int, input().split())
s = 0
for i in n:
    if i%2==1:
        if i%3==1:
            s+=0
        elif i%3==0:
            s+=0
        else:
            s+=2
    else:
        if i%3==1:
            s+=1
        elif i%3==0:
            s+=3
        else:
            s+=1
print(s)
