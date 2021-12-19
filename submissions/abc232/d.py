"""
" author : kaneshige
" created : 19.12.2021 20:50:33
"""

import sys
import itertools
from collections import deque


def main():
    h,w = map(int,readline().split())
    C = [list(readline().rstrip()) for _ in range(h)]

    s = (0,0,1)
    q = deque()
    q.append(s)

    to = [(0,1),(1,0)]

    #ans = [[-1]*w for _ in range(h)]
    v = set()
    v.add(s)
    ans = 1

    while q:
        x,y,z = q.popleft()
        t = True
        for dx,dy in to:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < h and 0 <= ty < w and (tx,ty) not in v:
                if C[tx][ty] == ".":
                    #ans[tx][ty] = max(ans[x][y] + 1,ans[tx][ty])
                    if t:
                        ans = max(ans,z+1)
                    t = False
                    #print((tx,ty))
                    q.append((tx,ty,z+1))
                    v.add((tx,ty))

    print(ans)

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
