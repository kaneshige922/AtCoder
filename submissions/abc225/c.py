
n,m = map(int,input().split())
B = [list(map(int,input().split())) for i in range(n)]





for i in range(n):
    for j in range(m-1):
        if B[i][j] + 1 != B[i][j+1]:
            print("No")
            exit()
    if B[i][m-1]%7 != 0:
        if B[i][0] % 7 > B[i][m-1] % 7:
            print("No")
            exit()
    if B[i][0]%7 == 0:
        if B[i][m-1]%7 > 0:
            print("No")
            exit()
for j in range(m):
    for i in range(n-1):
        if B[i][j] + 7 != B[i+1][j]:
            print("No")
            exit()

print("Yes")
