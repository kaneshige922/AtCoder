import sys
import itertools
from collections import deque


def main():
    n,m,d = map(int,readline().split())

    ans = (n-d)*(m-1)/(n**2)
    if d != 0:
        ans *= 2

    print("{:.7f}".format(ans))

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
