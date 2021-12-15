from collections import deque

n = int(input())

path = [[]for i in range(n)]
kyori = {}
for i in range(n-1):
    a,b,c = map(int,input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)
    kyori[tuple(sorted([a-1,b-1]))] = c

q,k = map(int,input().split())
xy = [list(map(int,input().split())) for i in range(q)]

#木のBFS→ダイクストラ
qu = deque([k-1])
v = set([k-1])
ans= [0 for i in range(n)]

while qu:
    h = qu.popleft()
    for i in path[h]:
        if i not in v:
            ans[i] = ans[h] + kyori[tuple(sorted([h,i]))]
            v.add(i)
            qu.append(i)


for i in xy:
    print(ans[i[0]-1]+ans[i[1]-1])


