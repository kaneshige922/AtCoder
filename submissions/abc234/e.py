"""
" author : kaneshige
" created : 08.01.2022 20:52:12
"""

import sys
import itertools
from collections import deque


def main():
    x = readline().rstrip()
    size_x = len(x)
    int_x = int(x)

    if size_x <= 2:
        print(x)
        exit()


    for i in range(1,10):
        for j in range(-8,9):
            if i + j*(size_x-1) < 0 or i + j*(size_x-1) > 9:
                continue
            s = []
            for k in range(size_x):
                s.append(str(i+j*k))
            s = int("".join(s))
            if s >= int_x:
                print(s)
                exit()

    print("1"*(size_x+1))












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
