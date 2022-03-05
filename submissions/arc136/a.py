"""
" author : kaneshige
" created : 27.02.2022 20:55:26
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    s = deque(list(readline().rstrip()))
    ans = []

    while s:
        h = s.popleft()

        if h == "C" or h == "A":
            ans.append(h)
        else:
            if s:
                if s[0] == "A":
                    ans.append(s.popleft())
                    s.appendleft(h)
                elif s[0] == "B":
                    s.popleft()
                    ans.append("A")
                else:
                    ans.append(h)
            else:
                ans.append(h)

    print("".join(ans))




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
