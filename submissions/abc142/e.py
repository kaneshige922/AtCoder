"""
" author : kaneshige
" created : 26.02.2022 14:45:05
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush
from copy import deepcopy

def main():
    n,m = map(int,readline().split())
    dist = [INF]*(2**n)
    edge = []
    for i in range(m):
        a,b = map(int,readline().split())
        c = list(map(int,readline().split()))
        edge.append([a,c])

    qu = [(0,0)]
    while qu:
        path_len,v = heappop(qu)
        for a,c in edge:
            w = deepcopy(v)
            for i in c:
                if not((v >> (i-1)) & 1):
                    w += 2**(i-1)
            if path_len+a < dist[w]:
                dist[w] = path_len + a
                heappush(qu,(path_len+a,w))

    if dist[2**n-1] == INF:
        print(-1)
    else:
        print(dist[2**n-1])




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
