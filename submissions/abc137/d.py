"""
" author : kaneshige
" created : 25.02.2022 21:57:23
"""
import heapq
import sys
import itertools
from collections import deque
from heapq import heappop,heappush

def main():
    n,m = map(int,readline().split())
    ab = [list(map(int,readline().split())) for _ in range(n)]
    ab.sort(key=lambda x:(x[0],-x[1]))

    qu = deque(ab)
    ans = 0
    hq = []
    for i in range(1,m+1):
        while qu:
            if qu[0][0] <= i:
                heappush(hq,-qu.popleft()[1])
            else:
                break
        if len(hq) != 0:
            ans += -heapq.heappop(hq)

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
