n = int(input())
a = list(map(int,input().split()))

import itertools 
def ruisekiwa(a):
    return list(itertools.accumulate(a))

a.sort()
aa = ruisekiwa(a)


cost = sum(a)
ans = cost

for i in range(1,n+1):
    x = a[i-1]/2
    ans = min(x*i+cost-aa[i-1]-x*(n-i),ans)

print(ans/n)
