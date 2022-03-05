"""
" author : kaneshige
" created : 02.03.2022 18:30:50
"""

import sys
import itertools
from collections import deque


def main():
    n = int(readline())
    x = readline().rstrip()

    pc = 0
    for i in range(1,n+1):
        if int(x[-i]):
            pc += 1
    #print(pc)
    pcl = [0,0]
    for i in range(1,n+1):
        if int(x[-i]):
            if pc != 1:
                pcl[0] += pow(2,i-1,pc-1)
                pcl[0] %= pc-1
            pcl[1] += pow(2,i-1,pc+1)
            pcl[1] %= pc+1
    #print(pcl)
    dp = [-1]*(pc+1)
    dp[0] = 0

    def saiki(X):
        if dp[X] != -1:
            return dp[X]
        p = 0
        for j in range(20):
            if X >> j & 1:
                p += 1
        dp[X] = saiki(X%p)+1
        return dp[X]

    ans = []

    for i in range(1,n+1):
        if int(x[-i]):
            if pc == 1:
                ans.append(0)
                continue
            x_i = pcl[0] - pow(2,i-1,pc-1)
            x_i %= pc-1

        else:
            x_i = pcl[1] + pow(2,i-1, pc+1)
            x_i %= pc+1
        ans.append(1+saiki(x_i))

    ans.reverse()
    for i in ans:
        print(i)



if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    sys.setrecursionlimit(10**6)
    true_ceil = lambda x, y: (x + y - 1) // y
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
