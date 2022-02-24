"""
" author : kaneshige
" created : 05.02.2022 01:06:43
"""

import sys
import itertools
from collections import deque
from bisect import bisect_left


def main():
    n = int(readline())
    dic = {}
    s = set()
    xc = [list(map(int,readline().split())) for _ in range(n)]
    xc.sort()
    for x,c in xc:
        s.add(c)
        if c in dic:
            dic[c].append(x)
        else:
            dic[c] = [x]
    S = sorted(list(s))

    h = 0
    ans = [[[0,0],[0,0]]]

    for s in S:
        i = dic[s]
        ad = [[0,0],[0,0]]
        ad[0][1] = i[0]
        ad[0][0] = min(ans[-1][0][0]+abs(i[-1]-ans[-1][0][1])+abs(i[-1]-i[0])
                       ,ans[-1][1][0]+abs(i[-1]-ans[-1][1][1])+abs(i[-1]-i[0]))
        ad[1][1] = i[-1]
        ad[1][0] = min(ans[-1][0][0]+abs(i[0]-ans[-1][0][1])+abs(i[-1]-i[0])
                       ,ans[-1][1][0]+abs(i[0]-ans[-1][1][1])+abs(i[-1]-i[0]))
        ans.append(ad)

    fa = min([a+abs(b) for a,b in ans[-1]])
    print(fa)

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
