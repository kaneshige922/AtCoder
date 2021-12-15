
h,w,c = map(int,input().split())
g = [list(map(int,input().split())) for i in range(h)]

# #a##
# ####
# ###b

ans = float("inf")

cost = [[g[j][i]-c*(i+j) for i in range(w)] for j in range(h)]

dp = [[float("inf") for i in range(w)] for j in range(h)]



for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            dp[i][j] = cost[i][j]
        elif i == 0:
            dp[i][j] = min(dp[i][j-1],cost[i][j-1])
        elif j == 0:
            dp[i][j] = min(dp[i-1][j],cost[i-1][j])
        else:
            dp[i][j] = min(dp[i][j-1],cost[i][j-1],dp[i-1][j],cost[i-1][j])

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        ans = min(ans,dp[i][j]+g[i][j]+c*(i+j))

#print(dp)
#print(ans)

cost = [[g[i][j]+c*(i-j) for j in range(w)] for i in range(h)]
dp = [[float("inf") for i in range(w)] for j in range(h)]


for i in range(h-1,-1,-1):
    for j in range(w):
        if i == h-1 and j == 0:
            dp[i][j] = cost[i][j]
        elif i == h-1:
            dp[i][j] = min(dp[i][j-1],cost[i][j-1])
        elif j == 0:
            dp[i][j] = min(dp[i+1][j],cost[i+1][j])
        else:
            dp[i][j] = min(dp[i][j-1],cost[i][j-1],dp[i+1][j],cost[i+1][j])

#print(dp)
#print(ans) 

for i in range(h):
    for j in range(w):
        if i == h-1 and j == 0:
            continue
        ans = min(ans,dp[i][j]+g[i][j]-c*(i-j))

print(ans)
