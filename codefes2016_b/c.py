#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array
import collections
import heapq


AdjacentVertex = collections.namedtuple("AdjacentVertex", "vertex cost")
INF = 2 ** 31 - 1
NO_VERTEX = -1


# Prim法で頂点0からの最小全域木を求める
def compute_mst_prim(max_v, adj_list):
    # pred[u]は頂点uの「ひとつ前」の頂点を表す
    pred = collections.defaultdict(lambda: NO_VERTEX)
    # uとpred[u]を結ぶ辺の重みがkey[u]に入る
    key = collections.defaultdict(lambda: INF)
    key[0] = 0
    # 二分ヒープを優先度付きキューとして用いる
    pq = [(key[v], v) for v in range(max_v)]
    heapq.heapify(pq)
    # 優先度付きキューに頂点が入っているかを示す配列
    in_pq = array.array("B", (True for _ in range(max_v)))
    while pq:
        _, u = heapq.heappop(pq)
        in_pq[u] = False
        for v, v_cost in adj_list[u]:
            if in_pq[v]:
                weight = v_cost
                if weight < key[v]:
                    pred[v] = u
                    key[v] = weight
                    heapq.heappush(pq, (weight, v))
                    in_pq[v] = True
    return (pred, key)


def main():
    W, H = list(map(int, input().split()))
    # max_v, max_e = map(int, input().split())
    max_v = (W+1) * (H+1)
    max_e = (W+1)*H + (H+1)*W
    adjacency_list = collections.defaultdict(set)
    for _w in range(W):
        p = int(input())
        for _h in range(H):
            adjacency_list[_w*H+_h].add(AdjacentVertex((_w+1)*H+_h, p))
            adjacency_list[(_w+1)*H+_h].add(AdjacentVertex(_w*H+_h, p))
    for _h in range(H):
        q = int(input())
        for _w in range(W):
            adjacency_list[_w*H+_h].add(AdjacentVertex((_w+1)*H+_h, q))
            adjacency_list[(_w+1)*H+_h].add(AdjacentVertex(_w*H+_h, q))
    # for _ in range(max_e):
    #     s, t, w = map(int, input().split())
    #     adjacency_list[s].add(AdjacentVertex(t, w))
    #     adjacency_list[t].add(AdjacentVertex(s, w))
    (_, key) = compute_mst_prim(max_v, adjacency_list)
    print(sum(key.values()))


if __name__ == '__main__':
    main()

