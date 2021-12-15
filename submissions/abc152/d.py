n = int(input())
ns = str(n)
nlen = len(str(n))

ans = 0

dp = [[0]*10 for i in range(10)]


for i in range(1,10):
    for j in range(1,10):
        cnt = 0
        for k in range(1,nlen):
            if k == 1:
                if i == j:
                    cnt += 1
            else:
                cnt += 10**(k-2)
        if i > int(ns[0]):
            pass
        elif i < int(ns[0]):
            cnt += 10**(nlen-2)
        else:
            for k in range(1,nlen-1):
                cnt += int(ns[k])*(10**(nlen-2-k))
            if int(ns[nlen-1]) >= j:
                cnt += 1
        dp[i][j] = cnt 

for i in range(1,10):
    for j in range(1,10):
        ans += dp[i][j]*dp[j][i]


#print(dp)
print(ans)
