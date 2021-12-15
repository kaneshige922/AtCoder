n = int(input())
ten = []
for i in range(n):
    ten.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if not(i == j or j == k or k == i):
                if (ten[k][1]-ten[i][1])*(ten[j][0]-ten[i][0]) == (ten[j][1]-ten[i][1])*(ten[k][0]-ten[i][0]):
                    print("Yes")
                    exit()
print("No")
