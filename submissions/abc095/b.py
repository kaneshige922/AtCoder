import sys
import itertools
from collections import deque
from copy import deepcopy


def main():
    n,c = map(int,readline().split())
    L1 = []
    L2 = []
    for i in range(n):
        x,v = map(int,readline().split())
        L1.append([x,v])
        L2.append([x-c,v])

    L2.reverse()

    L1c = [[0,0]]
    for i,j in L1:
        L1c.append([i,j-(i-L1c[-1][0])+L1c[-1][1]])
    #print(L1c)
    L1c2 = deepcopy(L1c)
    for i in range(1,n+1):
        if L1c2[i][1] <= L1c2[i-1][1]:
            L1c2[i] = L1c2[i-1]

    L2c = [[0,0]]
    for i,j in L2:
        L2c.append([i, j + (i - L2c[-1][0])+L2c[-1][1]])
    L2c2 = deepcopy(L2c)
    for i in range(1,n+1):
        if L2c2[i][1] <= L2c2[i-1][1]:
            L2c2[i] = L2c2[i-1]
    L2c.reverse()
    L2c2.reverse()
    #print(L2c)

    ans = 0
    for i,j in L1c:
        ans = max(ans,j)
    for i,j in L2c:
        ans = max(ans,j)
    for i in range(n+1):
        ans = max(ans,L1c[i][1]+L2c2[i][1]
                  -L1c[i][0])
        ans = max(ans,L1c2[i][1]+L2c[i][1]
                  +L2c[i][0])

    print(ans)



    """
    L = L1+L2
    print(L)
    kcl = [L[0][1]-L[0][0]]
    for i in range(1,2*n):
        if i < n:
            kcl.append(kcl[-1]+L[i][1]-L[i][0]+L[i-1][0])
        else:
            kcl.append(kcl[-1] + L[i][1] - L[i][0] + L[i - 1][0]
                       -L[i-n][1] + L[i-n+1][0] - L[i - n][0])
    
    print(kcl)
    """



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
