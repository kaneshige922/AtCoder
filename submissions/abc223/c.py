n = int(input())
ab = []
time = []

for i in range(n):
    a,b = map(int,input().split())
    ab.append([a,b])
    time.append(a/b)

ts = sum(time)

cnt = 0
ans = 0
for i in range(n):
    if cnt + time[i] > ts/2:
        ans += (ts/2-cnt)*ab[i][1]
        break
    else:
        cnt += time[i]
        ans += ab[i][0]

print(ans)

