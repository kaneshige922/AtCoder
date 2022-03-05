"""
" author : kaneshige
" created : 02.03.2022 21:20:55
"""

import sys
import itertools
from collections import deque
from copy import deepcopy


def main():
    n,k = map(int,readline().split())
    a = [0]+list(map(int,readline().split()))
    a2 = sorted(list(itertools.accumulate(a)))
    #print(a2)
    L = []
    for i in range(1,n+1):
        for j in range(i,n+1):
            L.append(a2[j]-a2[i-1])

    #print(sorted(L))
    L = deque(L)
    al = len(L)

    ans = 0
    for i in range(40,-1,-1):
        cnt = 0
        for j in range(al):
            h = L.popleft()
            if h >> i & 1:
                cnt += 1
            L.append(h)

        if cnt >= k:
            ans += pow(2,i)
            itr = deepcopy(al)
            for j in range(itr):
                h = L.popleft()
                if h >> i & 1:
                    L.append(h)
                else:
                    al -= 1
        #print(ans)
    print(ans)

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
