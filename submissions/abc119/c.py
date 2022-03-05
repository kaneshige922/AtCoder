"""
" author : kaneshige
" created : 01.03.2022 22:45:55
"""

import sys
import itertools
from collections import deque


def main():
    n, a, b, c = map(int, readline().split())
    l = []
    for i in range(n):
        l.append(int(readline()))
    l.sort()

    ans = INF

    for i in range(4**n):
        A = 0
        B = 0
        C = 0
        cnt = [0,0,0]
        for j in range(n):
            if not(i >> (2*j) & 1) and not(i >> (2*j+1) & 1):
                if A != 0:
                    cnt[0] += 10
                A += l[j]
            elif not(i >> (2*j) & 1) and (i >> (2*j+1) & 1):
                if B != 0:
                    cnt[1] += 10
                B += l[j]
            elif (i >> (2*j) & 1) and not(i >> (2*j+1) & 1):
                if C != 0:
                    cnt[2] += 10
                C += l[j]
        if A == 0 or B == 0 or C == 0:
            continue
        cnt[0] += abs(A-a)
        cnt[1] += abs(B-b)
        cnt[2] += abs(C-c)
        ans = min(ans,sum(cnt))
        

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
