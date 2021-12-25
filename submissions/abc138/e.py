"""
" author : kaneshige
" created : 22.12.2021 01:07:19
"""

import sys
import itertools
from collections import deque
from bisect import bisect_right


def main():
    s = readline().rstrip()
    t = readline().rstrip()

    S_LEN = len(s)
    T_LEN = len(t)

    dic = {}
    for i in range(S_LEN):
        if s[i] in dic:
            dic[s[i]].append(i+1)
        else:
            dic[s[i]] = [i+1]

    p = 0
    ans = 0

    for i in range(T_LEN):
        if t[i] not in dic:
            print(-1)
            exit()
        b = bisect_right(dic[t[i]],p)
        if b == len(dic[t[i]]):
            ans += S_LEN - p + dic[t[i]][0]
            p = dic[t[i]][0]
        else:
            ans += dic[t[i]][b] - p
            p = dic[t[i]][b]

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
