n = int(input())

ab = [list(map(int,input().split())) for i in range(n)]

dif = []

for i in ab:
    dif.append([i[0],1])
    dif.append([i[0]+i[1],-1])

dif.sort()

ans = {}
for i in range(n+1):
    ans[i] = 0
cnt = 0
for i in range(len(dif)):    
    ans[cnt] += dif[i][0] - dif[i-1][0]
    cnt +=  dif[i][1]

ans2 = []
for i in ans:
    if i != 0:
        ans2.append(ans[i])

print(*ans2)
