n = int(input())

ans = 0
if n == 1:
    print(1)
    exit()
for i in range(1,n):
    if n - i**2< 0:
        break
    ans += (n-i**2)//(2*i) +1

    
print(ans%998244353)
