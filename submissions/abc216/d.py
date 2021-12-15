from collections import deque
import sys
sys.setrecursionlimit(2*10**5)

n,m = map(int,input().split())

tama = []

for i in range(m):
    k = int(input())
    tama.append(deque(list(map(int,input().split()))))

col = {}

queue = deque()
for i in range(m):
    to = tama[i].popleft()-1
    if  to in col:
        queue.append((col[to],i))
    col[to] = i


v = set()

def saiki(a):
    if a not in v:
        if len(col[a]) == 2:
            v.add(a)
            for j in range(2):
                try:
                    b = tama[col[a][j]].popleft()-1
                    col[b].append(col[a][j])
                    saiki(b)
                except:
                    pass

cnt = 0

while queue:
    h = queue.popleft()
    for j in range(2):
        try:
            to = tama[h[j]].popleft()-1
            if to in col:
                queue.append((col[to],h[j]))
            col[to] = h[j]
        except:
            pass
    cnt += 1

        

if cnt == n:
    print("Yes")
else:
    print("No")

