"""
" author : kaneshige
" created : 20.02.2022 20:55:56
"""

import sys
import itertools
from collections import deque
def saiki(x):
    #print(x)
    if leaf[x] != 0:
        return leaf[x]
    cnt = 0
    for i in g[x]:
        if i not in v:
            v.add(i)
            cnt += 1
            leaf[x] += saiki(i)
    if cnt == 0:
        leaf[x] = 1

    return leaf[x]



def main():
    saiki(0)
    #print(leaf)
    ans = [[] for i in range(n)]
    ans[0] = [1,leaf[0]]
    qu2 = deque()
    qu2.append([0,1,leaf[1]])
    v2 = set()
    v2.add(0)

    while qu2:
        h,l,r = qu2.popleft()
        for i in g[h]:
            if i not in v2:
                v2.add(i)
                qu2.append([i,l,l+leaf[i]-1])
                ans[i] = [l,l+leaf[i]-1]
                l = l+leaf[i]

    for i in ans:
        print(*i)


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
    n = int(readline())
    g = [[] for i in range(n)]
    for i in range(n-1):
        u,v = map(int,readline().split())
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    leaf = [0 for i in range(n)]
    v = set()
    v.add(0)
    main()
