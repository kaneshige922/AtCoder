"""
" author : kaneshige
" created : 04.03.2022 00:13:47
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    d = list(map(int,readline().split()))
    cnt = [0]*13
    cnt[0] = 1
    for i in d:
        cnt[i] = min(3,cnt[i]+1)
    
    for i in range(13):
        if i == 0 or i == 12:
            if cnt[i] >= 2:
                print(0)
                exit()
        else:
            if cnt[i] >= 3:
                print(0)
                exit()
    ans = 0
    for i in range(2**13):
        t = [0]*24
        t[0] = 1
        for j in range(13):
            if cnt[j] == 2:
                t[j] = 1
                if j != 0:
                    t[24-j] = 1
            elif cnt[j] == 1:
                if j == 0 or j == 12:
                    t[j] = 1
                else:
                    if i >> j & 1:
                        t[j] = 1
                    else:
                        t[24-j] = 1
        s = 100
        for j in range(23):
            for k in range(j+1,24):
                if t[j] >= 1 and t[k] >= 1:
                    s = min(s,min(k-j,24-(k-j)))

        ans = max(ans,s)

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
