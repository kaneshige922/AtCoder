import numpy


n = int(input())

a = list(map(int,input().split()))
aa = numpy.cumsum(a)
s = sum(a)

ans = float("inf")

for i in range(n-1):
    ans = min(ans,abs(s-2*aa[i]))

print(ans)
