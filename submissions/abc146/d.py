from collections import deque

n = int(input())
miti = []
path = [[]for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    miti.append(tuple(sorted([a-1,b-1])))
    path[a-1].append(b-1)
    path[b-1].append(a-1)

queue = deque()
v = set()
zisu = [0]*n
col = [0]*n
dic = {}

queue.append(0)
v.add(0)

#BFS
while queue:
    h =queue.popleft()
    for i in path[h]:
        if i not in v:
            queue.append(i)
            v.add(i)
            zisu[h] +=1; zisu[i] +=1
            col[h] += 1; col[i] = col[h]
            dic[tuple(sorted([h,i]))] = col[h]

mz = max(zisu)
print(mz)
for i in miti:
    print(dic[i]%mz+1)


