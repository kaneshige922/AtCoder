
h,w,d = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]

dic = {}

for i in  range(h):
    for j in range(w):
        dic[a[i][j]] = [i,j]

dp = [0]*(h*w+1)

for i in range(1,h*w+1):
    if i <= d:
        dp[i] = 0
    else:
        dp[i] = dp[i-d] + abs(dic[i][0]-dic[i-d][0]) + abs(dic[i][1]-dic[i-d][1])

q = int(input())
ans = []

for i in range(q):
    l,r = map(int,input().split())
    ans.append(dp[r]-dp[l])

for i in ans:
    print(i)
