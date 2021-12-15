n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

adic = {}
bdic = {}
cdic = {}
for i in range(46):
    adic[i] = 0
    bdic[i] = 0
    cdic[i] = 0
for i in range(n):
    adic[a[i]%46] += 1
    bdic[b[i]%46] += 1
    cdic[c[i]%46] += 1

ans = 0

for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0:
                ans += adic[i]*bdic[j]*cdic[k]

print(ans)
