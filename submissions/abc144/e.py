n,k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))

a.sort()
f.sort(reverse=True)

#print(a)
#print(f)

mcost = 0

for i in range(n):
    mcost = max(mcost,a[i]*f[i])

#print(cost)

left = -1
right = mcost
mid = (left+right)//2

while right-left>1:
    cnt = 0
    for i in range(n):
        cnt += max(a[i]-mid//f[i],0)
    if cnt > k:
        left = mid
    else:
        right = mid
    mid = (left+right)//2

print(right)
