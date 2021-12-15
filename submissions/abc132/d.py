import sys
import itertools
from collections import deque
from math import factorial


def comb(n, r, p = 10**9+7):
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
    for r in range(1, k + 1):
        if n == k and r == 1:
            print(1)
            continue
        blue = comb(k - 1, r - 1) % MOD
        red1 = comb(n - k - 1, r) % MOD
        red2 = comb(n - k - 1, r - 1) % MOD
        ans = blue*(red1+2*red2)%MOD
        if r >= 2:
            red3 = comb(n - k - 1, r - 2) % MOD
            ans += blue*red3%MOD        #print(blue,red1,red2)

        print(ans%MOD)




if __name__ == "__main__":
    "----------Constants------------"
    INF = (1 << 62) - 1
    MOD = 10 ** 9 + 7
    # MOD = 998244353
    sys.setrecursionlimit(10**4)
    "----------Input------------"
    readline = sys.stdin.readline
    "----------Run------------"
    main()
