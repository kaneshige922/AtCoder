import sys
import itertools
from collections import deque


def main():
    n,p = map(int,readline().split())
    a = list(map(int,readline().split()))

    ans = 0
    for i in a:
        if i < p:
            ans += 1

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
