"""
" author : kaneshige
" created : 29.01.2022 21:28:29
"""

import sys
import itertools
from collections import deque
from bisect import bisect_left


def main():
    n = int(readline())
    s = list(readline().rstrip())
    dic = {}
    for i in range(n):
        if s[i] in dic:
            dic[s[i]].append(i)
        else:
            dic[s[i]] = [i]
    #rint(dic)
    r = n
    for i in range(n):
        if i >= r:
            break
        for j in range(97,ord(s[i])):
            if chr(j) in dic:
                p = bisect_left(dic[chr(j)],r)
                #print(r,p)
                if p != 0 and  i < dic[chr(j)][p-1]:
                    r = dic[chr(j)][p-1]
                    s[dic[chr(j)][p-1]] = s[i]
                    s[i] = chr(j)
                    break
        #print("".join(s))

    print("".join(s))



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
