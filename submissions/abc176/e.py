import sys
import itertools
from collections import deque,defaultdict
from heapq import heappush,heappop


def main():
    H,W,M = map(int,readline().split())
    hd = defaultdict(int)
    wd = defaultdict(int)
    v = set()
    for i in range(M):
        h,w = map(int,readline().split())
        v.add((h,w))
        hd[h] += 1
        wd[w] += 1
    hdl = []
    wdl = []

    for i in hd:
        heappush(hdl,[-hd[i],i])
    for i in wd:
        heappush(wdl,[-wd[i],i])

    cntmax = -(hdl[0][0] + wdl[0][0])

    h1 = heappop(hdl)
    ans = 0
    while 1:
        for w1 in wdl:
            s = -(h1[0]+w1[0])-((h1[1],w1[1]) in v)
            if ans - s >= 1:
                break
            ans = max(ans,-(h1[0]+w1[0])-((h1[1],w1[1]) in v))
        if len(hdl) == 0 or ans >= cntmax:
            break
        h1 = heappop(hdl)

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
