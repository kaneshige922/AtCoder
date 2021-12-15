n,C = map(int,input().split())

abc = [list(map(int,input().split())) for i in range(n)]

dic = {}

for a,b,c in abc:
    if a in dic:
        dic[a] += c
    else:
        dic[a] = c
    if b+1 in dic:
        dic[b+1] -= c
    else:
        dic[b+1] = -c

L = []


for i in dic:
    L.append([i,dic[i]])
L.sort()
Llen = len(L)

for i in range(1,Llen):
    L[i][1] += L[i-1][1]

ans = 0

for i in range(Llen-1):
    ans += min(C,L[i][1])*(L[i+1][0]-L[i][0])


print(ans)
