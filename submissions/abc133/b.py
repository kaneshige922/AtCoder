n,d = map(int,input().split())

import math

x = [list(map(int,input().split())) for i in range(n)]


ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        a = 0
        for k in range(d):
            a += (x[i][k]-x[j][k])**2
        if  int(math.sqrt(a))**2 == a:
            ans += 1

print(ans)
