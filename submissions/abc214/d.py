"""
" author : kaneshige
" created : 02.03.2022 15:50:05
"""

import sys
import itertools
from collections import deque

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets



def main():
    n = int(readline())
    e = []
    for i in range(n-1):
        u,v,w = map(int,readline().split())
        e.append([u-1,v-1,w])
    e.sort(key=lambda x:x[2])

    UF = DisjointSetUnion(n)
    ans = 0
    for u,v,w in e:
        s1 = UF.size[UF.find(u)]
        s2 = UF.size[UF.find(v)]
        ans += s1*s2*w
        UF.union(u, v)


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
