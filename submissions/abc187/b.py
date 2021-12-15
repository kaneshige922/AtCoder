n = int(input())
dot = []
for i in range(n):
    dot.append(list(map(int,input().split())))

ans = 0

for i in range(n-1):
    for j in range(i+1,n):
        if abs(dot[j][1]-dot[i][1]) <= abs(dot[j][0]-dot[i][0]):
            ans +=1
print(ans)
