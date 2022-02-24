"""
" author : kaneshige
" created : 06.02.2022 03:09:45
"""

import sys
import itertools
from collections import deque
from bisect import bisect_left


def main():
    a,b,q = map(int,readline().split())
    s = [int(readline()) for _ in range(a)]
    t = [int(readline()) for _ in range(b)]
    s.sort()
    t.sort()

    for i in range(q):
        x = int(readline())
        ans = INF
        d = INF
        "ê_é–Å®éõ"
        p = bisect_left(s,x)
        if p != 0:
            d = abs(x-s[p-1])
            p2 = bisect_left(t,s[p-1])
            if p2 == 0:
                d += abs(s[p-1]-t[p2])
            elif p2 == b:
                d += abs(s[p-1]-t[p2-1])
            else:
                d += min(abs(s[p-1]-t[p2-1]),abs(s[p-1]-t[p2]))
        ans = min(ans,d)
        if p != a:
            d = abs(x - s[p])
            p2 = bisect_left(t, s[p])
            if p2 == 0:
                d += abs(s[p] - t[p2])
            elif p2 == b:
                d += abs(s[p]-t[p2-1])
            else:
                d += min(abs(s[p]-t[p2-1]), abs(s[p]-t[p2]))
        ans = min(ans, d)
        p = bisect_left(t, x)
        if p != 0:
            d = abs(x-t[p-1])
            p2 = bisect_left(s,t[p-1])
            if p2 == 0:
                d += abs(t[p-1]-s[p2])
            elif p2 == a:
                d += abs(t[p-1]-s[p2-1])
            else:
                d += min(abs(t[p-1]-s[p2-1]),abs(t[p-1]-s[p2]))
        ans = min(ans,d)
        if p != b:
            d = abs(x - t[p])
            p2 = bisect_left(s, t[p])
            if p2 == 0:
                d += abs(t[p] - s[p2])
            elif p2 == a:
                d += abs(t[p]-s[p2-1])
            else:
                d += min(abs(t[p]-s[p2-1]), abs(t[p]-s[p2]))
        ans = min(ans, d)
        print(ans)

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
