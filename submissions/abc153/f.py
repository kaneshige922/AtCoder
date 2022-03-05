"""
" author : kaneshige
" created : 26.02.2022 15:17:32
"""
import heapq
import sys
import itertools
from collections import deque
from heapq import heappop,heappush

def main():
    n,d,a = map(int,readline().split())
    xh = sorted([list(map(int,readline().split())) for _ in range(n)])


    ans = true_ceil(xh[0][1],a)
    hq = []
    heappush(hq,[xh[0][0],true_ceil(xh[0][1],a)*a])
    heappush(hq, [xh[0][0]+2*d+1, -(true_ceil(xh[0][1],a)*a)])


    if n >= 2:
        damage = 0
        for x,h in xh[1:]:
            while hq[0][0] <= x:
                damage += heappop(hq)[1]
                if len(hq) == 0:
                    break
            if h > damage:
                ans += true_ceil(h-damage, a)
                heappush(hq, [x, true_ceil(h-damage, a) * a])
                heappush(hq, [x+2*d+1,-true_ceil(h-damage,a)*a])

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
