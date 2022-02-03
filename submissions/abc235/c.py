"""
" author : kaneshige
" created : 15.01.2022 20:58:04
"""

import sys
import itertools
from collections import deque


def main():
    n,q = map(int,readline().split())
    a = list(map(int,readline().split()))
    dic = {}
    for i in range(n):
        if a[i] in dic:
            dic[a[i]].append(i)
        else:
            dic[a[i]] = [i]

    for i in range(q):
        x,k = map(int,readline().split())
        if x not in dic:
            print(-1)
            continue
        if len(dic[x]) < k:
            print(-1)
        else:
            print(dic[x][k-1]+1)



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
