import bisect

n = int(input())
l = list(map(int,input().split()))

l.sort()
ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        right = i
        left  = bisect.bisect_right(l,l[j]-l[i],0,i)
        ans += right-left

print(ans)
