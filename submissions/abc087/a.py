n = int(input())
a = [list(map(int,input().split())) for i in range(2)]

ans = [[0]*n for i in range(2)]

ans[0][0] = a[0][0]

for i in range(1,n):
    ans[0][i] = ans[0][i-1] + a[0][i]

ans[1][0] = ans[0][0] + a[1][0]

for i in range(1,n):
    ans[1][i] = max(ans[0][i],ans[1][i-1]) + a[1][i]

print(ans[1][n-1])
