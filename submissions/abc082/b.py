
S = list(input())
X,Y = map(int,input().split())

x = 0
y = 0
to = [(1,0),(0,1),(-1,0),(0,-1)]
t = 0
xl = []
yl = []
for s in S:
    if s == "F":
        if t == 0:
            x += 1
        else:
            y += 1
    else:
        if t == 0:
            xl.append(x)
            x = 0
            t = 1
        else:
            yl.append(y)
            y = 0
            t = 0
if t == 0:
    xl.append(x)
    x = 0
    t = 1
else:
    yl.append(y)
    y = 0
    t = 0

#print(xl)
#print(yl)


#MLE
"""""
N = 16001
n = N//2

xdp = [[0 for i in range(N)] for i in range(len(xl)+1)]
ydp = [[0 for i in range(N)] for i in range(len(yl)+1)]
xdp[0][n] = 1
ydp[0][n] = 1

for i in range(len(xl)):
    for j in range(N):
        if xdp[i][j] == 1:
            if i == 0:
                xdp[i+1][j+xl[i]] = 1
            else:
                xdp[i+1][j-xl[i]] = 1
                xdp[i+1][j+xl[i]] = 1

for i in range(len(yl)):
    for j in range(N):
        if ydp[i][j] == 1:
            ydp[i+1][j-yl[i]] = 1
            ydp[i+1][j+yl[i]] = 1


if xdp[len(xl)][X+n] and ydp[len(yl)][Y+n]:
    print("Yes")
else:
    print("No")
"""

v = set([0])

for i in range(len(xl)):
    L = list(v)
    v = set()
    for j in L:
        if i == 0:
            v.add(j+xl[i])
        else:
            v.add(j-xl[i])
            v.add(j+xl[i])

w = set([0])

for i in range(len(yl)):
    L = list(w)
    w = set()
    for j in L:
        w.add(j-yl[i])
        w.add(j+yl[i])

if X in v and Y in w:
    print("Yes")
else:
    print("No")
