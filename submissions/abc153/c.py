n,k = map(int,input().split())
h = list(map(int,input().split()))

h.sort()
if n <= k:
    print(0)
    exit()

ans = sum(h[:(n-k)])

print(ans)
