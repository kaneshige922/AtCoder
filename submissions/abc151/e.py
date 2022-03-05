"""
" author : kaneshige
" created : 02.03.2022 01:12:15
"""

import sys
import itertools
from collections import deque


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 10 ** 6  # N ‚Í•K—v•ª‚¾‚¯—pˆÓ‚·‚é
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


def main():
    n,k = map(int,readline().split())
    a = list(map(int,readline().split()))
    a.sort()
    ans = 0

    for j in range(n):
        if j >= k-1:
            ans += a[j]*cmb(j,k-1,p)
            ans %= MOD
        if j <= n-k:
            ans -= a[j]*cmb(n-j-1,k-1,p)
            ans %= MOD

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
