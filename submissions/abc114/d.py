"""
" author : kaneshige
" created : 02.03.2022 17:44:34
"""

import sys
import itertools
import collections
from collections import deque
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a




def main():
    n = int(readline())
    d = {}
    prime = []
    for i in range(1,n+1):
        l =  prime_factorize(i)
        for j in l:
            if j not in d:
                prime.append(j)
                d[j] = 1
            else:
                d[j] += 1
    #print(prime)
    prime.sort()
    #print(d)
    b = [[2,4,4],[0,4,14],[0,2,24],[0,0,74]]

    ans = set()

    for i,j,k in b:
        for x in prime:
            for y in prime:
                for z in prime:
                    if x == y or y == z or z == x:
                        continue
                    f = [0,0,0,i,j,k]
                    if i != 0:
                        if d[x] >= i:
                            f[0] = x
                        else:
                            continue
                    if j != 0:
                        if d[y] >= j:
                            f[1] = y
                        else:
                            continue
                    if d[z] >= k:
                        f[2] = z
                    else:
                        continue
                    if j == k:
                        if y > z:
                            f[1],f[2] = f[2],f[1]
                    ans.add(tuple(f))
    print(len(list(ans)))

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
