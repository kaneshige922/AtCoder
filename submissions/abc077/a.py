import bisect
import numpy as np

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
bc = []
cc = []
for i in a:
    bc.append(n-bisect.bisect_right(b,i))
for i in b:
    cc.append(n-bisect.bisect_right(c,i))

cc.reverse()
cc = list(np.cumsum(cc))
cc.reverse()

ans = 0

for i in bc:
    if i > 0:
        ans += cc[-i]

print(ans)
