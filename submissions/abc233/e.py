"""
" author : kaneshige
" created : 25.12.2021 20:46:20
"""

import sys
#import itertools
#from collections import deque
#import time


def main():
    #ST = time.time()
    #x = "9"*(5*100000-1)
    #x = [int(i) for i in list(x)]
    x = [int(i) for i in list(readline().rstrip())]
    #print(time.time() - ST)
    ans = [0]*(len(x)+10)

    sum_x = sum(x)

    def saiki(r):
        if ans[r] >= 10:
            ans[r-1] += 1
            ans[r] -= 10
            saiki(r-1)
        else:
            return
    lx = len(x)
    for i in range(lx):
        ans[-(i + 1)] += sum_x
        ans[-(i + 2)] += ans[-(i + 1)] // 10
        ans[-(i + 1)] = ans[-(i + 1)] % 10
        sum_x -= x[-(i + 1)]

    #print(time.time() - ST)

    #print(ans)


    for i in range(len(ans)):
        ans[i] = str(ans[i])


    print(int("".join(ans)))



    #print(time.time()-ST)

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
