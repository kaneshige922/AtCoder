"""
" author : kaneshige
" created : 15.01.2022 20:58:20
"""

import sys
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
    UF = UnionFind(n)

    edge.sort()

    for d,e,f,g,h in edge:
        if UF.same(e,f):
            continue
        if g == 0:
            UF.unite(e,f)
        else:
            ans[h] = 1

    for i in ans:
        if i:
            print("Yes")
        else:
            print("No")




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
    n,m,q = map(int,readline().split())

    edge = []

    for i in range(m):
        a,b,c = map(int,readline().split())
        edge.append([c,a-1,b-1,0,0])
    for i in range(q):
        u,v,w = map(int,readline().split())
        edge.append([w,u-1,v-1,1,i])

    ans = [0]*q

    main()
