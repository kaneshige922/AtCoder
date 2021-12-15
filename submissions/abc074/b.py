


n = int(input())

a = [list(map(int,input().split())) for i in range(n)]

edge = [[float("inf") for i in range(n)] for i in range(n)]

for i in range(n-1):
    for j in range(i+1,n):
        if i == 0:
            edge[i][j] = a[i][j]
        else:
            cost = float("inf")
            for k in range(i):
                cost = min(cost,a[k][i]+a[k][j])

            if cost < a[i][j]:
                print(-1)
                exit()
            elif cost == a[i][j]:
                pass
            else:
                edge[i][j] = a[i][j]
                for k in range(i):
                    if a[k][j] == a[k][i] + a[i][j]:
                        edge[k][j] =  float("inf")
                    elif  a[k][j] > a[k][i] + a[i][j]:
                        print(-1)
                        exit()
                    if a[k][i] == a[k][j] + a[i][j]:
                        edge[k][i] =  float("inf")
                    elif  a[k][i] > a[k][j] + a[i][j]:
                        print(-1)
                        exit()
                    


#print(edge)

ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        if edge[i][j] != float("inf"):
            ans += edge[i][j]

print(ans)
