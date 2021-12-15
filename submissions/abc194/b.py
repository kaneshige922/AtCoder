n = int(input())
ab = []
ans = 2*(10**5)
for i in range(n):
    a1,b1 = map(int,input().split())
    ab.append([a1,b1])
for i in range(n):
    for j in range(n):
        if i == j:
            time = ab[i][0] + ab[j][1]
        else:
            time = max(ab[i][0],ab[j][1])
        ans = min(ans,time)
print(ans)
