n,d = map(int,input().split())
t = [list(map(int,input().split())) for i in range(n)]

ans = 0

for i in range(n):
    if t[i][0]**2 + t[i][1]**2 <= d**2:
        ans +=1

print(ans)
