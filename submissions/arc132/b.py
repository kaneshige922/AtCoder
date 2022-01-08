"""
" author : kaneshige
" created : 26.12.2021 20:53:01
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    p = list(map(int, readline().split()))
    A = [i for i in range(1, n + 1)]
    B = [n - i for i in range(n)]
    cnt0 = 0
    cnt1 = 0
    flag = False
    for i in range(n - 1):
        if p[i] == 1:
            if p[i]+2 > p[i-1]:
                flag = True
            break
        elif p[i + 1] == 1:
            if p[i+1]+2 > p[i]:
                flag = True
            break

    #print(flag)

    cnt = 0
    for i in range(n):
        if p[i] == 1:
            break
        cnt += 1

    #print(cnt)
    if flag:
        ans = cnt + 1 + 1
        ans = min(ans,n-(cnt+1)+1)
    else:
        ans = cnt
        ans = min(ans,n-cnt+2)

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
