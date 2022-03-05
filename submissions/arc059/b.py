"""
" author : kaneshige
" created : 03.03.2022 22:36:54
"""

import sys
import itertools
from collections import deque


def main():
    s = readline().rstrip()
    qu = deque([s[0]])

    for i in range(1,len(s)):
        if i <= 1:
            qu.append(s[i])
            if qu[0] == qu[-1]:
                print(1,2)
                exit()
        else:
            if qu[0] == s[i] or qu[-1] == s[i]:
                print(i-1,i+1)
                exit()
            else:
                qu.append(s[i])
                qu.popleft()

    print(-1,-1)



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
