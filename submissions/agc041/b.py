n,m,v,p = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse=True)

s = sum(a[p-1:])

#print(s)
#print(*a)

right = n
left = p-1
mid = (right+left)//2

while right-left > 1:
    cost = 0
    cnt = 0
    t = True
    for i in range(n):
        if i <= p-2:
            cnt += 1
        elif mid <= i:
            cnt += 1
        else:
            cost += m-(a[i]-a[mid])
            if m-(a[i]-a[mid]) < 0:
                t = False
    cost2 = v*m - m*(min(cnt,v))
    if cost >= cost2 and t:
        left = mid
    else:
        right = mid
    mid = (right+left)//2

print(left+1)
