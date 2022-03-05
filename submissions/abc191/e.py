"""
" author : kaneshige
" created : 03.03.2022 23:11:29
"""

import sys
import itertools
from collections import deque
from heapq import heappop, heappush


def dijkstra(graph, start):
    """
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [INF] * n, [-1] * n

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v] or v == start:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))
    #print(dist)
    return dist, parents


def main():
    for s in range(n):
        d,p = dijkstra(g,s)
        if d[s] == INF:
            print(-1)
        else:
            print(d[s])

if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    n, m = map(int, readline().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, readline().split())
        g[a - 1].append([b - 1, c])
    main()
