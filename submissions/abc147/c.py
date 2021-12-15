
import sys
sys.setrecursionlimit(10**6)

mod = 10 ** 9 + 7
mod2 = 998244353

n = int(input())

A = []
for i in range(n):
    a = int(input())
    li = []
    for j in range(a):
        x,y = map(int,input().split())
        li.append([x-1,y])
    A.append(li)


ans = 0
for i in range(2**n):
    t = True
    cnt = 0
    for j in range(n):
        if i >> j & 1:
            cnt += 1
            for x,y in A[j]:
                if (i>>x&1) != y:
                    t = False
                    break
        if not(t):
            break
    if t:
        ans = max(ans,cnt)

print(ans)
