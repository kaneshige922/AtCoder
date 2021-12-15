n = int(input())
a = [list(map(int,input().split())) for i in range(n)]

ans = 1
mod = 1000000007

for i in range(n):
    x = sum(a[i])%mod
    ans = (ans*x)%mod

print(ans)
