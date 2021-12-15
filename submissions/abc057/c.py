n = int(input())
m = n**0.5

ans = 11

for i in range(1,n+1):
    if i > m:
        break
    if n % i == 0:
        v = len(str(n//i))
        ans = min(ans,v)

print(ans)
