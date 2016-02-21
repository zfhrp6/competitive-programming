n = int(input())
mochis = []
for i in range(n):
    mochis.append(int(input()))

stack = []
mochis.sort()

for _mochi in mochis:
    if sum(stack) < _mochi:
        stack.append(_mochi)

print(len(stack))