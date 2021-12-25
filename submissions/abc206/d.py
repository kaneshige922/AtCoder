"""
" author : kaneshige
" created : 22.12.2021 01:48:41
"""

import sys
import itertools
from collections import deque

#Unionfind-tree
#n = 100#—v‘f”n‚ğéŒ¾


class UnionFind:
    def __init__(self,n):
        self.par = [-1 for _ in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self,x):
        if self.par[x] == -1:
            return x
        else:
            return self.find(self.par[x])
    def unite(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            else:
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
    def same(self,x,y):
        if self.find(x) == self.find(y):
            return True
        else:
            return False


def main():
    n = int(readline())
    A = list(map(int,readline().split()))

    T = UnionFind(2*10**5)

    for i in range(n//2):
        if A[i] != A[-i-1]:
            T.unite(A[i]-1,A[-i-1]-1)

    ans = [0]*(2*10**5)

    for i in range(2*10**5):
        ans[T.find(i)] += 1

    fa = 0
    for i in range(2 * 10 ** 5):
        fa += max(0,ans[i]-1)

    print(fa)


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
