import sys
sys.setrecursionlimit(10000000)

a,b = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

dp = [[[-1,-1]for i in range(b+1)] for j in range(a+1)]
dp[0][0] = [0,0]

def saiki(x,y):
    if dp[x][y] != [-1,-1]:
        return dp[x][y]
    else:
        if x==0:
            z = saiki(x,y-1)
            dp[x][y][0] = z[1] + B[-y]
            dp[x][y][1] = z[0]
        elif y == 0:
            z = saiki(x-1,y)
            dp[x][y][0] = z[1] + A[-x]
            dp[x][y][1] = z[0]
        else:
            z1 = saiki(x,y-1)
            z2 = saiki(x-1,y)
            if z1[1] + B[-y] >= z2[1] + A[-x]:
                dp[x][y][0] = z1[1]+B[-y]
                dp[x][y][1] = z1[0]
            else:
                dp[x][y][0] = z2[1]+A[-x]
                dp[x][y][1] = z2[0]
        return dp[x][y]



print(saiki(a,b)[0])
