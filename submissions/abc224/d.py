import sys
sys.setrecursionlimit(10**6)


from collections import deque
from copy import deepcopy

m = int(input())
g = [[] for i in range(9)]
for i in range(m):
    u,v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

pl = list(map(int,input().split()))

p = [9]*9
for i in range(8):
    p[pl[i]-1] = i+1

s = -1
for i in range(9):
    if p[i] == 9:
        s = i

v = set()

ac = "123456789"



p = "".join([str(i) for i in p])

if p == ac:
    print(0)
    exit()


dic = {}
dic[p] = 0
v.add(p)
qu = deque([p])

while qu:
    h = qu.popleft()
    idx = -1
    for i in range(9):
        if h[i] == "9":
            idx = i
            break
    for i in g[idx]:
        if i < idx:
            l2 = h[:i] + h[idx] + h[i+1:idx] + h[i] + h[idx+1:]
        else:
            l2 = h[:idx] + h[i] + h[idx+1:i] + h[idx] + h[i+1:]
        if l2 not in v:
            v.add(l2)
            dic[l2] = 1
            dic[l2] += dic[h]
            qu.append(l2)
            if l2 == ac:
                print(dic[l2])
                exit()

print(-1)
