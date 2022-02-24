"""
" author : kaneshige
" created : 13.02.2022 20:56:22
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    s = list(map(int,readline().split()))
    s.reverse()
    a = [0]
    b = [0]
    c = [s[0]]
    for i in range(1,n):
        if i % 3 == 0:
            c.append(c[-1]+s[i]-s[i-1])
        elif i % 3 == 1:
            a.append(a[-1]+s[i]-s[i-1])
        else:
            b.append(b[-1] + s[i] - s[i - 1])

    #print(a,b,c)
    minl = [min(a),min(b),min(c)]
    cnt = [0,0,0]
    if sum(minl) < 0:
        print("No")
        exit()
    else:
        minl[1] += minl[0]
        cnt[0] -= minl[0]
        cnt[1] += minl[0]
        minl[2] += minl[1]
        cnt[1] -= minl[1]
        cnt[2] += minl[1]
    ans = []
    for i in range(n+2):
        if i % 3 == 0:
            ans.append(a[i//3]+cnt[0])
        elif i % 3 == 1:
            ans.append(b[i//3]+cnt[1])
        else:
            ans.append(c[i//3]+cnt[2])

    ans.reverse()
    print("Yes")
    print(*ans)


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
