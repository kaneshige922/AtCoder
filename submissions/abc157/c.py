n,m = map(int,input().split())
sc = [list(map(int,input().split())) for i in range(m)]

n1 = [[] for i in range(n)]

for i in range(m):
    if len(n1[sc[i][0]-1]) == 0:
        n1[sc[i][0]-1].append(sc[i][1])
    elif n1[sc[i][0]-1][0] != sc[i][1]:
        print(-1)
        exit()

ans = ""

for i in range(n):
    if i == 0:
        if len(n1[i]) > 0:
            if n1[i][0] == 0 and not(n == 1):
                print(-1)
                exit()
            else:
                ans += str(n1[i][0])
        else:
            if n == 1:
                ans += "0"
            else:
                ans += "1"
    else:
        if len(n1[i]) > 0:
            ans += str(n1[i][0])
        else:
            ans += "0"           
print(int(ans))
