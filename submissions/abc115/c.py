n,k = map(int,input().split())
h = [int(input()) for i in range(n)]
h.sort()


ans = 10**9
for i in range(k-1,n):
    ans = min(h[i]-h[i-k+1],ans)

print(ans)
