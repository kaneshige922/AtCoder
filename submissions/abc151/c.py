n,m = map(int,input().split())
ps = []
for i in range(m):
    p,s = input().split()
    p = int(p)
    ps.append([p,s])

ans = [[0,0] for i in range(n)]

for i in range(m):
    if ps[i][1] == "AC":
        ans[ps[i][0]-1][0] = 1
    else:
        if ans[ps[i][0]-1][0] == 0:
            ans[ps[i][0]-1][1] +=1

ac = wa = 0

for i in range(n):
    if ans[i][0] == 1:
        ac += 1
        wa += ans[i][1]

print(ac,wa)
