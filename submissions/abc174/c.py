import sys
import itertools
from collections import deque


def main():
    K = int(readline())
    p = 7 % K
    q = 7 % K
    v = {p}
    cnt = 1

    while 0 not in v:
        q = (10*q+p)%K
        cnt += 1
        if q in v:
            break
        else:
            v.add(q)

    if 0 in v:
        print(cnt)
    else:
        print(-1)


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
