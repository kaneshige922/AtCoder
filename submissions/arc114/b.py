
import sys
sys.setrecursionlimit(10**6)

mod = 10 ** 9 + 7
mod2 = 998244353

n = int(input())
f = list(map(int,input().split()))


v = set()
ans = 1 

for i in range(1,n+1):
    if i not in v:
        h = i
        v1 = set()
        while(1):
            v.add(h)
            v1.add(h)
            h = f[h-1]
            if h in v1:
                ans = (ans*2)%mod2
                break
            elif h in v:
                break




print((ans-1)%mod2)
