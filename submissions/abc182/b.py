n = int(input())
a = list(map(int,input().split()))

m = max(a)
m2 = 0
ans = 0

for i in range(2,m+1):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if m2 < count:
        m2 = count
        ans = i


print(ans)
