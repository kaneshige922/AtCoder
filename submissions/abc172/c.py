import sys
import itertools
from collections import deque



    


#if __name__ == "__main__":
"----------Constants------------"
INF = (1 << 62) - 1
MOD = 10 ** 9 + 7
# MOD = 998244353
sys.setrecursionlimit(10**5)
"----------Input------------"
#readline = sys.stdin.readline
readline = input
"----------Run------------"
N, M, K = map(int, readline().split())
A = list(map(int, readline().split()))
B = list(map(int, readline().split()))

A = list(itertools.accumulate(A))
B = [0] + list(itertools.accumulate(B)) + [INF]

ans = 0

for i in range(N + 1):
    if i >= 1:
        k = K - A[i - 1]
    else:
        k = K
    if k < 0:
        continue
    left = 0
    right = M + 1
    mid = (left + right) // 2
    while right - left > 1:
        if B[mid] <= k:
            left = mid
        else:
            right = mid
        mid = (left + right) // 2
    ans = max(ans, i + left)

print(ans)
