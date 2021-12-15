n,k = map(int,input().split())

ans = 0
for i in range(k,n+2):
    if i == 1:
        f = n+1
    else:
        f = n+1-(i-1)+(i-1)*n+(4-i)*(i-1)//2-((i+1)*i//2)+1
    if i >= k:
        ans += f
print(ans%(10**9+7))
