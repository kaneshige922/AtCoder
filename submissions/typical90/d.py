l,r = map(int,input().split())

mod = 1000000007

ans = 0

for i in range(1,20):
    if l >= 10**i or r < 10**(i-1):
        continue
    ans += i * (min(10**i-1,r)+max(10**(i-1),l))*(min(10**i-1,r)-max(10**(i-1),l)+1)//2
    ans %= mod

print(ans)
