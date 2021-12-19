"""
" author : kaneshige
" created : 19.12.2021 21:18:14
"""

import sys
import itertools
from collections import deque



def main():
    n, m = map(int, readline().split())
    g1 = [set() for _ in range(n)]
    g2 = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, readline().split())
        g1[a - 1].add(b - 1)
        g1[b - 1].add(a - 1)
    for i in range(m):
        a, b = map(int, readline().split())
        g2[a - 1].append(b - 1)
        g2[b - 1].append(a - 1)

    p = [_ for _ in range(n)]

    P = list(itertools.permutations(p))

    for q in P:
        t = True
        for i in range(n):
            for j in g2[i]:
                if q[j] not in g1[q[i]]:
                    t = False
                    break
            if not t:
                break
        if t :
            print("Yes")
            exit()
    print("No")



if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    # sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
