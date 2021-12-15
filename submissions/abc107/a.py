n,k = map(int,input().split())
x = list(map(int,input().split()))

ans = 10**15

for i in range(n-k+1):
    if x[i] >= 0:
        ans =min(ans,x[i+k-1])
    elif  x[i+k-1] < 0:
        ans =min(ans,abs(x[i]))
    else:
        y = min(abs(x[i]),abs(x[i+k-1]))
        ans = min(ans,x[i+k-1]-x[i]+y)

print(ans)
