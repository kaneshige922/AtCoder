"""
" author : kaneshige
" created : 02.03.2022 17:14:43
"""

import sys
import itertools
from collections import deque


def main():
    n,m = map(int,readline().split())
    cnt = 0
    ans = 0
    g = [[] for _ in range(n)]
    e = []
    for i in range(m):
        x,y,z = map(int,readline().split())
        g[x-1].append([y-1,z])
        g[y-1].append([x-1,z])
        e.append([x-1,y-1])

    v = set()
    for i in e:
        #print(i,cnt,ans)
        if i[0] in v:
            continue
        ans += 1
        cnt += 1
        qu = deque()
        qu.append(i[0])
        v.add(i[0])
        while qu:
            h = qu.popleft()
            for j,l in g[h]:
                if j not in v:
                    cnt += 1
                    v.add(j)
                    qu.append(j)

    print(ans+n-cnt)

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
