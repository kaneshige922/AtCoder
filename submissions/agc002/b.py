
import sys
sys.setrecursionlimit(10**6)

mod = 10 ** 9 + 7
mod2 = 998244353

n,m = map(int,input().split())
xy = []
for i in range(m):
    x,y = map(int,input().split())
    xy.append([x-1,y-1])

kosu = [1]*n
ans = set([0])

for x,y in xy:
    kosu[x] -= 1
    kosu[y] += 1
    if x in ans or y in ans:
        ans.add(y)
        if kosu[x] == 0 and x in ans:
            ans.discard(x)


print(len(ans))


