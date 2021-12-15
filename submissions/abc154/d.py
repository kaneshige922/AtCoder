n,k = map(int,input().split())
p = list(map(int,input().split()))

sums = sum(p[:k])
ans = sums

for i in range(1,n-k+1):
    sums -= p[i-1]
    sums+= p[i+k-1]
    ans = max(ans,sums)

print((ans+k)/2)
