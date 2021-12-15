n = int(input())
p = list(map(int,input().split()))

ans = 1
minp = p[0]
for i in range(1,n):
    if minp > p[i]:
        ans += 1
        minp = p[i]

print(ans)
