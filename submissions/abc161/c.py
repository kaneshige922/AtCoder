n,k = map(int,input().split())

n -= (n//k) * k

m = abs(n - k)

print(min(n,m))
