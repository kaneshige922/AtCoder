import numpy as np

n = int(input())
a = list(map(int,input().split()))

ac = np.cumsum(a)
acm = [ac[0]]
for i in range(1,n):
    acm.append(max(acm[i-1],ac[i]))
p = 0

ans = 0

for i in range(n):
    ans = max(ans,p+acm[i])
    p += ac[i]

print(ans)
