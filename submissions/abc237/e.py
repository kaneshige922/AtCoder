"""
" author : kaneshige
" created : 30.01.2022 21:24:18
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
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents


def main():
    d,p = dijkstra(g,0)
    print(-min(d))

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
    n,m = map(int,readline().split())
    h = list(map(int,readline().split()))
    g = [[] for _ in range(n)]
    for i in range(m):
        u,v = map(int,readline().split())
        if h[u-1] == h[v-1]:
            g[u-1].append([v-1,0])
            g[v - 1].append([u - 1, 0])
        elif h[u-1] > h[v-1]:
            g[u - 1].append([v - 1, -h[u-1]+h[v-1]])
            g[v - 1].append([u - 1, 2*(h[u-1]-h[v-1])])
        else:
            g[v - 1].append([u - 1, h[u - 1] - h[v - 1]])
            g[u - 1].append([v - 1, 2 * (h[v - 1] - h[u - 1])])
    #print(g)



    main()
