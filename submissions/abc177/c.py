n = int(input())
a = list(map(int,input().split()))


ans = 0
sums = sum(a)

for i in range(n-1):
    sums -= a[i]
    ans += a[i]*sums

print(ans % 1000000007)
