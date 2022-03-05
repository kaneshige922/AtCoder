"""
" author : kaneshige
" created : 24.02.2022 21:26:15
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    g = [[] for i in range(n)]
    for i in range(n-1):
        u,v,w = map(int,readline().split())
        g[u-1].append([v-1,w])
        g[v-1].append([u-1,w])

    qu = deque([0])
    v = {0}
    ans = [-1]*n
    ans[0] = 0
    while qu:
        h = qu.popleft()
        for i,d in g[h]:
            if i not in v:
                v.add(i)
                if d % 2 == 0:
                    ans[i] = ans[h]
                else:
                    ans[i] = not(ans[h])
                qu.append(i)
    for i in ans:
        print(int(i))

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
