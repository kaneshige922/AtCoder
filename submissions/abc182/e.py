h,w,n,m = map(int,input().split())

g = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    a,b = map(int,input().split())
    g[a-1][b-1] = 1

for j in range(m):
    c,d = map(int,input().split())
    g[c-1][d-1] = -1

#pprint(g)

for i in range(h):
    l = 0
    flag = False
    for j in range(w):
        if flag:
            if g[i][j] == 0:
                g[i][j] = 2
            elif g[i][j] == -1:
                flag = False
                l = j+1
        else:
            if g[i][j] == 1:
                flag = True
                for k in range(l,j):
                    g[i][k] = 2
            elif g[i][j] == -1:
                l = j+1

#pprint(g)

for j in range(w):
    l = 0
    flag = False
    for i in range(h):
        if flag:
            if g[i][j] == 0:
                g[i][j] = 2
            elif g[i][j] == -1:
                flag = False
                l = i+1
        else:
            if g[i][j] == 1:
                flag = True
                for k in range(l,i):
                    g[k][j] = 2
            elif g[i][j] == -1:
                l = i+1


#pprint(g)
ans = 0

for i in range(h):
    for j in range(w):
        if g[i][j] >= 1:
            ans += 1

print(ans)
