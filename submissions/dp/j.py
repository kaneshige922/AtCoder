import sys
sys.setrecursionlimit(1000000000)

n = int(input())

a = list(map(int,input().split()))

num = [0,0,0]
for i in a:
    num[i-1] += 1

dp = [[[-1 for k in range(n+1)]  for j in range(n+1)] for i in range(n+1)]

dp[0][0][0] = 0

def saiki(a,b,c):
    if a < 0 or b < 0 or c < 0:
        return 0
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    else:
        z = 0
        z += (n+(saiki(a-1,b,c)*a+saiki(a+1,b-1,c)*b+saiki(a,b+1,c-1)*c))/(a+b+c)
        dp[a][b][c] = z
        return dp[a][b][c]

print(saiki(num[0],num[1],num[2]))

