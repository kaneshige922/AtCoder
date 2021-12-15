import sys
import itertools
from collections import deque


def main():
    N = int(readline())
    d = {}
    for i in range(N):
        S = readline().rstrip()
        if S in d:
            d[S] += 1
        else:
            d[S] = 1
    ans = ""
    cnt = 0
    for i in d:
        if d[i] > cnt:
            ans = i
            cnt = d[i]

    print(ans)


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
