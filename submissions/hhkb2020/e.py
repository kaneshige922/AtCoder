"""
" author : kaneshige
" created : 25.02.2022 18:58:13
"""

import sys
import itertools
from collections import deque


def main():
    h,w = map(int,readline().split())
    s = [readline().rstrip() for _ in range(h)]

    cnt = 0

    H = [[-1] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                H[i].append(j)
            else:
                cnt += 1
        H[i].append(w)

    W = [[-1] for _ in range(w)]
    for i in range(w):
        for j in range(h):
            if s[j][i] == "#":
                W[i].append(j)
        W[i].append(h)

    P = [[0]*w for _ in range(h)]

    for i in range(h):
        l = -1
        r = H[i][1]
        idx = 1
        for j in range(w):
            if s[i][j] == ".":
                P[i][j] += r - l - 1
            else:
                l = H[i][idx]
                r = H[i][idx+1]
                idx += 1
    #print(P)
    for i in range(w):
        l = -1
        r = W[i][1]
        idx = 1
        for j in range(h):
            if s[j][i] == ".":
                P[j][i] += r - l - 2
            else:
                l = W[i][idx]
                r = W[i][idx + 1]
                idx += 1

    ans = 0

    d = {}

    for i in range(h):
        for j in range(w):
            if P[i][j] not in d:
                d[P[i][j]] = 1
            else:
                d[P[i][j]] += 1

    for i in d:
        ans += (d[i]*((pow(2,i,MOD)-1)%MOD)*pow(2,cnt-i,MOD))%MOD
        ans %= MOD



    '''
    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                ans += (((pow(2,P[i][j],MOD)-1)%MOD)*pow(2,cnt-P[i][j],MOD))%MOD
                ans %= MOD
    '''
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
