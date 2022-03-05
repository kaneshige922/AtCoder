"""
" author : kaneshige
" created : 26.02.2022 20:57:57
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    s = [readline().rstrip() for _ in range(n)]
    ans = False
    for i in range(n):
        for j in range(n):
            if j <= n-6:
                cnt = 0
                for k in range(6):
                    if s[i][j+k] == "#":
                        cnt += 1
                if cnt >= 4:
                    ans = True
            if i <= n-6:
                cnt = 0
                for k in range(6):
                    if s[i+k][j] == "#":
                        cnt += 1
                if cnt >= 4:
                    ans = True
            if i <= n-6 and j <= n-6:
                cnt = 0
                for k in range(6):
                    if s[i+k][j+k] == "#":
                        cnt += 1
                if cnt >= 4:
                    ans = True
            if i<= n-6 and j >= 5:
                cnt = 0
                for k in range(6):
                    if s[i+k][j-k] == "#":
                        cnt += 1
                if cnt >= 4:
                    ans = True
                    
    if ans:
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
