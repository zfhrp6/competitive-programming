#!/usr/bin/env python
from __future__ import print_function

def connected_components(graph):
    seen = set()
    def component(n):
        nodes = set([n])
        while nodes:
            n = nodes.pop()
            seen.add(n)
            nodes |= set(graph[n]) - seen
            yield n
    for n in graph:
        if n not in seen:
            yield component(n)

def print_gen(gen):
    print([list(x) for x in gen])

def check_connected(graph):
    import networkx as nx
    G = nx.Graph()
    G.add_nodes_from(graph.keys())
    for k, v in graph.items():
        for n in v:
            G.add_edge(k, n)
    check = sorted([set(x) for x in nx.connected_components(G)]) == sorted([set(x) for x in connected_components(graph)])
    print(check, "(equal to one derived from networkx)")

graph = {0: [1, 2, 3], 1: [2], 2: [], 3: [4, 6], 4: [], 5: [7], 6: [], 7: []}

print("graph =", graph)
print_gen(connected_components(graph))
check_connected(graph)
