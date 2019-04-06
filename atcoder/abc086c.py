import sys


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


N = int(input())
q = []
for i in range(N):
    q.append(tuple(list(map(int, input().split()))))
q = sorted(q)

tmp = (0, 0, 0)
for query in q:
    if (query[0] - tmp[0] < dist(tmp[1:], query[1:]) or (query[1] - tmp[1] + query[2] - tmp[2]) % 2 != (query[0] - tmp[0]) % 2):
        print('No')
        sys.exit()
else:
    print('Yes')
