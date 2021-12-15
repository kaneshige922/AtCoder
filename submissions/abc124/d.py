n,k = map(int,input().split())
s = input()

t = [[-1,-1]]
if s[0] == "0":
    t.append([0])

for i in range(n-1):
    if s[i] != s[i+1]:
        if s[i] == "0":
            t[-1].append(i)
        else:
            t.append([i+1])
if s[n-1] == "0":
    t[-1].append(n-1)
t.append([n,n])


ans = 0
if len(t)-2 <= k :
    print(n)
    exit()
if k == 1:
    for i in range(1,len(t)-k):
        ans = max(ans,t[i+1][0]-t[i-1][1]-1)
    print(ans)
    exit()
for i in range(1,len(t)-k):
    ans= max(ans,t[i+k][0]-t[i-1][1]-1)

print(ans)




