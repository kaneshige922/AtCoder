"""
" author : kaneshige
" created : 19.12.2021 20:49:04
"""

import sys
import itertools
from collections import deque


def main():
    s = readline().rstrip()
    t = readline().rstrip()

    v = set()

    for i in range(len(s)):
        if ord(s[i]) <= ord(t[i]):
            v.add(ord(t[i])-ord(s[i]))
        else:
            v.add(26+ord(t[i])-ord(s[i]))

    if len(list(v)) == 1:
        print("Yes")
    else:
        print("No")

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
