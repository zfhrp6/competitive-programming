class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = min(v1, v2)
        self.v2 = max(v1, v2)
        self.weight = weight
        self.isOdd = weight % 2 > 0
        self.isEven = not self.isOdd

    def __lt__(self, other):
        return (self.v1, self.v2) < (other.v1, other.v2)

White = True
Black = False

N = int(input())
edges = {}
colored_v = {}
uncolored_v = [x for x in range(1, N+1)]

for i in range(1, N):
    v1, v2, w = list(map(int, input().split()))
    edges[i] = Edge(v1, v2, w)


for _ in range(100):
    if len(uncolored_v) == 0:
        break
    colored_v[uncolored_v[0]] = White
    uncolored_v.remove(uncolored_v[0])
    for ek,ev in sorted(edges.items()):
        if ev.v1 not in colored_v and ev.v2 not in colored_v:
            continue
        if ev.v1 in colored_v and ev.v2 in colored_v:
            continue
        if ev.v1 in colored_v:
            s, e = ev.v1, ev.v2
        else:
            s, e = ev.v2, ev.v1
        if ev.isEven:
            colored_v[e] = colored_v[s]
        if ev.isOdd:
            colored_v[e] = not colored_v[s]
        uncolored_v.remove(e)




for v in sorted(colored_v.items()):
    print(0 if v[1] else 1)
