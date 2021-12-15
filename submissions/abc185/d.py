from collections import deque
import math

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a = deque(a)
a.append(n+1)
a.appendleft(0)
sa = deque()


for i in range(m+1):
    if a[i+1]-a[i]-1 > 0:
        sa.append(a[i+1]-a[i]-1)

#—áŠOˆ—
if len(sa)==0:
    print(0)
    exit()


haba = min(sa)
ans = 0
while sa:
    t = sa.popleft()
    ans += math.ceil(t/haba)

print(ans)
