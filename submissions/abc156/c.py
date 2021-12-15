n = int(input())
x = list(map(int,input().split()))

maxx = max(x)

ans = 100**3

for i in range(1,maxx+1):
    sums = 0 
    for j in range(n):
        sums += (x[j]-i)**2
    ans = min(ans,sums)

print(ans) 
