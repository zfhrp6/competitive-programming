from bisect import bisect_left
from collections import deque
from itertools import islice


N, M = list(map(int, input().split()))
As = list(map(int, input().split()))
cards = {}
for i in range(N):
    cards[As[i]] = cards.get(As[i], 0) + 1
# sorted_keys = deque(sorted(cards.keys()))
sorted_keys = list(sorted(cards.keys()))

for i in range(M):
    b, c = list(map(int, input().split()))
    cnt = 0
    # for k in islice(sorted_keys,0,bisect_left(sorted_keys, c)):
    for k in sorted_keys[0:bisect_left(sorted_keys, c)]:
        for _ in range(cards.get(k,0)):
            cards[k] = cards[k] - 1
            if cards[k] == 0:
                del(cards[k])
                sorted_keys.remove(k)
            cards[c] = cards.get(c, 0) + 1
            if c not in sorted_keys:
                sorted_keys.insert(bisect_left(sorted_keys, c),c )
            cnt += 1
            if cnt >= b:
                break
        if cnt >= b:
            break

print(sum([k * cnt for k,cnt in cards.items()]))


