"""
" author : kaneshige
" created : 30.12.2021 02:29:58
"""

import sys
import math
import itertools
from collections import deque

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
    N,K = map(int,readline().split())
    a = [list(map(int,readline().split())) for _ in range(N)]
    
    "s‚Ì•À‚×•û--------------------------------"
    U1 = UnionFind(N)
    for i in range(N-1):
        for j in range(i+1,N):
            is_swap = True
            for k in range(N):
                if a[i][k] + a[j][k] > K:
                    is_swap = False
                    break
            if is_swap:
                U1.unite(i,j)
    cnt1 = [0]*N
    for i in range(N):
        cnt1[U1.find(i)] += 1
    ans = 1
    for i in cnt1:
        ans *= math.factorial(i)%MOD
        ans %= MOD
    "—ñ‚Ì‘I‚Ñ•û---------------------------------"
    U2 = UnionFind(N)
    for i in range(N - 1):
        for j in range(i + 1, N):
            is_swap = True
            for k in range(N):
                if a[k][i] + a[k][j] > K:
                    is_swap = False
                    break
            if is_swap:
                U2.unite(i, j)
    cnt2 = [0] * N
    for i in range(N):
        cnt2[U2.find(i)] += 1
    for i in cnt2:
        ans *= math.factorial(i) % MOD
        ans %= MOD


    print(ans)


if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    #MOD = 10 ** 9 + 7
    MOD = 998244353
    # sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
