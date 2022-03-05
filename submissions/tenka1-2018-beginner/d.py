"""
" author : kaneshige
" created : 02.03.2022 00:47:53
"""

import sys
import itertools
from collections import deque

def sol(x):
    for i in range(10**3):
        if i*(i-1) == 2*x:
            return True,i
    return False,-1


def main():
    n = int(readline())
    t,c = sol(n)

    if t:
        print("Yes")
        print(c)
        d = [[] for _ in range(c)]
        cnt = 1
        for i in range(c-1):
            for j in range(i+1,c):
                d[i].append(cnt)
                d[j].append(cnt)
                cnt += 1

        for i in d:
            print(len(i),*i)
    else:
        print("No")
        


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
