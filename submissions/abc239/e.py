"""
" author : kaneshige
" created : 19.02.2022 20:56:20
"""

import sys
import itertools
from collections import deque
from heapq import heappop,heappush
from copy import deepcopy


def saiki(nu):
    global ans
    #print(ans)
    if len(ans[nu]) != 0:
        return ans[nu]
    heappush(ans[nu], x[nu])
    for i in g[nu]:
        if i not in v:
            v.add(i)
            sa = deepcopy(saiki(i))
            while sa:
                ad = heappop(sa)
                if len(ans[nu]) < 20:
                    heappush(ans[nu],ad)
                else:
                    bd = heappop(ans[nu])
                    if ad > bd:
                        heappush(ans[nu],ad)
                    else:
                        heappush(ans[nu],bd)
    return ans[nu]

def main():

    saiki(0)
    #print(ans)
    fa = [[] for i in range(n)]
    for i in range(n):
        while len(ans[i]) != 0:
            fa[i].append(heappop(ans[i]))
    #print(fa)
    for i in range(q):
        V,k = map(int,readline().split())
        print(fa[V-1][-k])





if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    n, q = map(int, readline().split())
    x = list(map(int, readline().split()))
    g = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, readline().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    num = [[] for i in range(n)]

    s = 0
    v = set()
    v.add(0)
    ans = [[] for i in range(n)]
    main()
