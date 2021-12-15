h,n = map(int,input().split())

ab = []
for i in range(n):
    a,b = map(int,input().split())
    ab.append([a,b])

ab = sorted(ab,key=lambda x:x[1])

#while(h>=ab[0][0]):

dp = [0 for i in range(h+1)]

def myceil(a,b):
    return a//b + (a%b!=0)

for i in range(n):
    for j in range(h+1):
        if i == 0:
            dp[j] = myceil(j,ab[0][0])*ab[0][1]
        else:
            if j < ab[i][0]:
                dp[j] = min(dp[j],myceil(j,ab[i][0])*ab[i][1])
            else:
                dp[j] = min(dp[j-ab[i][0]]+ab[i][1],dp[j])



print(dp[h])

