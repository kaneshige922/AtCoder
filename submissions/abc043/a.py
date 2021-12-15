n = int(input())
a = list(map(int,input().split()))

mi = min(a)
ma = max(a)

ans = 10**9

for i in range(mi,ma+1):
    s = 0 
    for j in a:
        s += (j-i)**2
    ans = min(ans,s)

print(ans)
