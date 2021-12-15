n,k = map(int,input().split())


ans = 0
if k == 0:
    ans = n**2
    print(ans)
    exit()

for i in range(k+1,n+1):
    ans += (n//i)*(i-k) + max(0,n%i-k+1)

print(ans)
