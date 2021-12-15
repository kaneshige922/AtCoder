c = [list(map(int,input().split())) for i in range(3)]

for i in range(1,3):
    if not(c[i][0]-c[i-1][0] == c[i][1]-c[i-1][1] and  c[i][2]-c[i-1][2] == c[i][1]-c[i-1][1]):
        print("No")
        exit()

for i in range(1,3):
    if not(c[0][i]-c[0][i-1] == c[1][i]-c[1][i-1] and  c[2][i]-c[2][i-1] == c[1][i]-c[1][i-1]):
        print("No")
        exit()

print("Yes")
