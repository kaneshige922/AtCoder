n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))


ans = [10**9]*n
if n == 1:
    print(t[0])
    exit()

for i in range(n):
    ans[i] = min(ans[i-1]+s[i-1],t[i])
ans[0] = min(ans[n-1]+s[n-1],t[0])
for i in range(n):
    ans[i] = min(ans[i-1]+s[i-1],t[i])
ans[0] = min(ans[n-1]+s[n-1],t[0])

for i in ans:
    print(i)
