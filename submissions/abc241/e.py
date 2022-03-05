"""
" author : kaneshige
" created : 26.02.2022 20:58:08
"""

import sys
import itertools
from collections import deque
from copy import deepcopy

def main():
    n,k = map(int,readline().split())
    a = list(map(int,readline().split()))
    x = 0
    l = [0]
    p = [a[0]]
    v = {0}
    while k != 0:
        k -= 1
        x += a[x%n]

        if x%n in v:
            #print(p, x % n)
            idx = -1
            rs = 0
            t = False
            for i in range(len(p)):
                if x%n == l[i]:
                    idx = deepcopy(i)
                    rs += p[i]
                    t = True
                elif t:
                    rs += p[i]

            rp = len(p)-idx
            #print(k, idx,rp,rs,k%rp)
            x += rs*(k//rp)
            x += sum(p[idx:(idx+k%rp)])
            break

        v.add(x%n)
        l.append(x % n)
        p.append(a[x%n])

    #print(p)
    print(x)

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
