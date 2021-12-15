import sys
import itertools
from collections import deque


def main():
    n,m = map(int,readline().split())
    g = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,readline().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    for i in range(n):
        if len(g[i]) >= 3:
            print("No")
            exit()

    v = set()
    parent = [i for i in range(n)]
    #print(g)
    for i in range(n):
        if i in v:
            continue
        if len(g[i]) == 0:
            continue
        qu = deque([i])
        v.add(i)
        while qu:
            h = qu.popleft()
            for j in g[h]:
                if j not in v:
                    v.add(j)
                    qu.append(j)
                    parent[j] = h
                elif j != parent[h]:
                    print("No")
                    exit()

    print("Yes")






if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    #sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
