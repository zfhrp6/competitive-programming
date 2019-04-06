n,m = list(map(int, input().split()))
uv = []
for i in range(m):
    uv.append(tuple(map(int, input().split())))

# print(uv)
print(n**2-m*2)
