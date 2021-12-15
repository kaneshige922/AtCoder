n,x = map(int,input().split())
alco = []
for i in range(n):
    alco.append(list(map(int,input().split())))

ans = -1
x = 100*x
for i in range(n):
    x -= alco[i][0]*alco[i][1]
    if x < 0:
        ans = i+1
        break
print(ans)
