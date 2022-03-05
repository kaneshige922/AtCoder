"""
" author : kaneshige
" created : 01.03.2022 21:48:29
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    g = [[] for _ in range(n)]
    edge = []
    for i in range(n-1):
        a,b = map(int,readline().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
        edge.append([a-1,b-1])
    d = [0]*n

    qu = deque([0])
    v = {0}
    while qu:
        h = qu.popleft()
        for i in g[h]:
            if i not in v:
                d[i] = d[h] + 1
                qu.append(i)
                v.add(i)

    q = int(readline())
    w = [0]*n
    for i in range(q):
        t,e,x = map(int,readline().split())
        if t == 1:
            if d[edge[e-1][0]] < d[edge[e-1][1]]:
                w[0] += x
                w[edge[e - 1][1]] -= x
            else:
                w[edge[e - 1][0]] += x
        else:
            if d[edge[e-1][0]] > d[edge[e-1][1]]:
                w[0] += x
                w[edge[e - 1][0]] -= x
            else:
                w[edge[e - 1][1]] += x

    qu = deque([0])
    v = {0}
    while qu:
        h = qu.popleft()
        for i in g[h]:
            if i not in v:
                w[i] += w[h]
                qu.append(i)
                v.add(i)

    for i in w:
        print(i)

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
    main()
