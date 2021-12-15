import numpy as np

n = int(input())
d= list(map(int,input().split()))

dm = max(d)

dlis = [0]* dm

for i in range(n):
    dlis[d[i]-1] += 1

dlis2 = list(np.cumsum(dlis))

ans = 0

for i in range(dm):
    if float(dlis2[i]) == n/2:
        ans += 1
    if float(dlis2[i]) > n/2:
        break

print(ans)
