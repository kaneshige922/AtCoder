import numpy  as  np
import bisect

n,k= map(int,input().split())
a = list(map(int,input().split()))

wa = [0] + list(np.cumsum(a))
ans = 0

for i in range(1,n+1):
    a = bisect.bisect_left(wa,k+wa[i-1],i,n+1) 
    ans += n+1-a


print(ans)


