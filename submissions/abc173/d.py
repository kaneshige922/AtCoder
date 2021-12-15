n = int(input())
a = list(map(int,input().split()))

b = sorted(a,reverse=True)

ans = b[0]

for i in range(1,(n-2)//2+1):
        ans += 2*b[i]
if  n % 2 == 1:
    ans += b[(n-2)//2+1]

print(ans)
