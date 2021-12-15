import math

n,k = map(int,input().split())

ans = 0
for i in range(1,n+1):
    if k >= i:
        ans += (1/n) * (1/2)**(math.ceil(math.log(k/i,2)))
    else:
        ans += 1/n

print(ans)
