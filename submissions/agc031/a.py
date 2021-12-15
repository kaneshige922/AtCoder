import sys
sys.setrecursionlimit(10**6)

mod = 10 ** 9 + 7
mod2 = 998244353

n = int(input())
s = list(input())

dic = {}

for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

ans = 1

for i in dic:
    ans = ans*(dic[i]+1)%mod


print(ans-1)
