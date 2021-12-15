n =int(input())
a = list(map(int,input().split()))

a.sort()

s = sum(a)
ans = 0

for i in range(n):
    ans += s - a[i]*(n-i)
    s -= a[i]

print(ans)
