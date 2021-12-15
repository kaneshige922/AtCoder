import bisect
import math
n = int(input())
a = list(map(int,input().split()))

a.sort()

x = a[-1]

b = bisect.bisect_right(a,math.ceil(x/2))

if a[b]-math.ceil(x/2) >= math.ceil(x/2)-a[b-1]:
    print(x,a[b-1])
else:
    print(x,a[b])
