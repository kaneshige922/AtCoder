"""
" author : kaneshige
" created : 19.02.2022 20:56:15
"""

import sys
import itertools
from collections import deque

def sosu(x):
    if x < 2:
        return 0
    if x == 2:
        return 1
    t = 1
    for i in range(2,x):
        if i**2 > x:
            break
        if x % i == 0:
            t = 0
            break
    return t




def main():
    a,b,c,d = map(int,readline().split())

    l = []

    for i in range(a+c,b+d+1):
        l.append(sosu(i))
    #print(l)
    cnt = sum(l[:d-c+1])
    #print(cnt)
    if cnt == 0:
        print("Takahashi")
        exit()
    left = 0
    right = d-c+1
    for i in range(b-a):
        cnt -= l[left]
        cnt += l[right]
        if cnt == 0:
            print("Takahashi")
            exit()
        left += 1
        right += 1

    print("Aoki")




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
