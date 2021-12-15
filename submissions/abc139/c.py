n = int(input())
h = list(map(int,input().split()))

h.reverse()

ans = 0
count = 0

for i in range(1,n):
    if h[i-1] <= h[i]:
        count += 1
        ans = max(ans,count)
    else:
        count = 0

print(ans)
