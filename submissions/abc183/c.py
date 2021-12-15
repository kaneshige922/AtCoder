import itertools


n,k = map(int,input().split())
t = []
for i in range(n):
    t.append(list(map(int,input().split())))
nlist = [i for i in range(1,n)]
zyun = list(itertools.permutations(nlist))

ans = 0

for i in zyun:
    tim = 0
    tim += t[0][i[0]]
    for j in range(1,n-1):
        tim += t[i[j-1]][i[j]]
    tim += t[i[n-2]][0]
    if tim == k:
        ans += 1

print(ans)
