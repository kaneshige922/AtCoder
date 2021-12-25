"""
" author : kaneshige
" created : 25.12.2021 20:46:14
"""

import sys
import itertools
from collections import deque,defaultdict


def main():
    n,k = map(int,readline().split())
    a = [0] + list(map(int,readline().split()))
    b = list(itertools.accumulate(a))
    dic = defaultdict(int)
    dic[0] += 1

    ans = 0

    for i in b[1:]:
        ans += dic[i-k]
        dic[i] += 1

    print(ans)



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
