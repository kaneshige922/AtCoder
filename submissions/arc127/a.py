n = int(input())
ns = str(n)
nlen = len(ns)

dp = [0 for i in range(nlen+1)]
dp[1] = 1

for i in range(2,nlen+1):
    dp[i] = 10**(i-1)+dp[i-1]
#print(dp)
if int(ns[0]) > 1:
    print(sum(dp))
else:
    ans = 0
    t = True
    t2 = True
    t2cnt = 1
    for i in range(1,nlen):
        ans += t2cnt*int(ns[i])*(10**(nlen-1-i))
        if int(ns[i]) == 1 and t2:
            t2cnt += 1
        if int(ns[i]) != 1:
            t2 = False
        if int(ns[i])==0:
            t = False
        if t and int(ns[i]) > 1:
            ans += dp[nlen-i]
            t = False
    ans += sum(dp[:-1])
    for i in ns:
        if int(i) == 1:
            ans += 1
        else:
            break
    print(ans)
