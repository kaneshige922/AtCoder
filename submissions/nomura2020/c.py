"""
" author : kaneshige
" created : 20.12.2021 23:10:44
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    a = list(map(int,readline().split()))
    a2 = list(itertools.accumulate(a))
    sum_a = sum(a)

    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    cnt = 0

    if a[0] > 0 and n != 0:
        print(-1)
        exit()
    elif n == 0:
        if a[0] == 1:
            print(1)
            exit()
        else:
            print(-1)
            exit()



    for i in range(1,n+1):
        dp[i] += min(2*dp[i-1],sum_a-cnt)-a[i]
        if dp[i] < 0:
            print(-1)
            exit()
        cnt += a[i]


    print(sum(dp)+sum_a)






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
