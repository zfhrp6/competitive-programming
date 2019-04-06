N = int(input())
As = list(map(int, input().split()))
ret = 3**N
tmp = 1
for a in As:
    if a % 2 == 0:
        tmp *= 2
print(ret-tmp)

