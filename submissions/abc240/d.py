"""
" author : kaneshige
" created : 20.02.2022 20:55:51
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    a = list(map(int,readline().split()))
    cnt = 1
    qu = deque([[a[0],1]])
    print(1)
    if n == 1:
        exit()
    for i in a[1:]:
        #print(qu)
        if qu:
            if qu[-1][0] == i:
                if qu[-1][1] == i-1:
                    m = qu.pop()
                    cnt -= m[1]
                else:
                    qu[-1][1] += 1
                    cnt += 1
            else:
                cnt += 1
                qu.append([i, 1])
        else:
            cnt += 1
            qu.append([i,1])
        print(cnt)




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
