n = int(input())
dist1 = []
dist2 = []
X = []
Y = []
for i in range(n):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

xmi = min(X)
yma = max(Y)

for i in range(n):
    dist1.append(X[i]+Y[i])
    dist2.append(X[i]-xmi+yma-Y[i])

dist1.sort(reverse=True)
dist2.sort(reverse=True)





print(max(dist1[0]-dist1[n-1],dist2[0]-dist2[n-1]))
