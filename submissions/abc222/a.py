import sys
import itertools
from collections import deque


def main():
    n = readline().rstrip()

    ans = "0"*(4-len(n)) + n
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
