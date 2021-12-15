import sys
import itertools
from collections import deque
from bisect import  bisect_left


def main():
    n,q = map(int,readline().split())
    a = list(map(int,readline().split()))
    a.sort()
    for i in range(q):
        x = int(readline())
        print(n-bisect_left(a,x))



if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    #sys.setrecursionlimit(10**6)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
