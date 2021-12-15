n = int(input())
a = list(map(int,input().split()))

ans = 0
tmax = 0


for i in range(n):
    if a[i] > tmax:
        tmax = a[i]
    else:
        ans += tmax - a[i]


print(ans)
