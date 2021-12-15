n = int(input())
s = list(input())

w = [0]*n
if s[0] == "W":
    w[0] += 1

for i in range(1,n):
    if s[i] == "W":
        w[i] = w[i-1]+1
    else:
        w[i] = w[i-1]

ans = n

for i in range(n):
    if i >=1:
        k = w[i-1] + n-i-1 - (w[n-1]-w[i])
        ans = min(ans,k)
    else:
        k = n-1 - (w[n-1]-w[0])
        ans = min(ans,k)

print(ans)
