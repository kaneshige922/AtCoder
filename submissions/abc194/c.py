n = int(input())
a = list(map(int,input().split()))

ans = 0

s1 = s2 = s3 = 0
s2 = sum(a)
for i in range(n-1):
    s1 += a[i]**2
    s2 -= a[i]
    s3 += s2*a[i]
s1 += a[n-1]**2
ans = (n-1)*s1 - 2*s3
print(ans)
