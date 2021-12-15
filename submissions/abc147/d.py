import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    a = list(map(int,readline().split()))
    cnt = [[0]*60 for i in range(2)]

    for i in a:
        for j in range(60):
            if i >> j & 1:
                cnt[1][j] += 1
            else:
                cnt[0][j] += 1
    ans = 0
    for i in range(60):
        ans += pow(2,i,MOD)*cnt[0][i]*cnt[1][i]%MOD
        ans %= MOD
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
