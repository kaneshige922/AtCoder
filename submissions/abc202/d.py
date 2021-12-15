a,b,k = map(int,input().split())

cij =  [[0]*(b+1) for i in range(a+1)]

for i in range(b+1):
    cij[0][i] = 1

for i in range(1,a+1):
    for j in range(b+1):
        cij[i][j] = int(cij[i-1][j]*(i+j)/i)

ans = []
def saiki(a,b,k):
    if a == 0:
        for i in range(b):
            ans.append("b")
        return
    if b == 0:
        for i in range(a):
            ans.append("a")
        return
    if cij[a-1][b] >= k:
        ans.append("a")
        return saiki(a-1,b,k)
    else:
        ans.append("b")
        return saiki(a,b-1,k-cij[a-1][b])

saiki(a,b,k)

print("".join(ans))
