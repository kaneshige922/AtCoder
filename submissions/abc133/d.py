n =int(input())
a = list(map(int,input().split()))
a = a+a
ans = [0 for i in range(n)]

ap = [0,a[0]]
am = [0,-a[0]]
for i in range(1,2*n):
    if i % 2 == 0:
        ap.append(ap[-1]+a[i])
        am.append(am[-1]-a[i])
    else:
        ap.append(ap[-1]-a[i])
        am.append(am[-1]+a[i])

for i in range(1,n+1):
    if i % 2 != 0:
        ans[i-1] = ap[n+i-1]-ap[i-1]
    else:
        ans[i-1] = am[n+i-1]-am[i-1]

print(*ans)
 
