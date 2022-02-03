"""
" author : kaneshige
" created : 30.01.2022 20:57:09
"""

import sys
import itertools
from collections import deque


def main():
    s = list(readline().rstrip())
    l = deque(s)

    t = True
    while l:
        if l[0] == l[-1]:
            if l[0] != "a":
                t = False
            l.popleft()
            if l:
                l.pop()
        elif t and l[-1] == "a":
            l.pop()
        else:
            break
    if not(l):
        print("Yes")
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
