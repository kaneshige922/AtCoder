from collections import deque

n = int(input())
ab = [[] for i in range(n)]
for i  in range(n-1):
    a,b = map(int,input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)
ab = [set(sorted(ab[i])) for i in range(n)]
q = deque()
v = set()
root = []
q.append(0)
root.append(1)
v.add(0)
tyokuzen = deque()
while q:
    h = q.popleft()
    t = True
    for i in ab[h]:
        if i not in v:
            q.append(i)
            v.add(i)
            root.append(i+1)
            tyokuzen.append(h)
            ab[h].remove(i)
            ab[i].remove(h)
            t = False
            break
    if t:
        if h == 0:
            print(*root)
            exit()
        else:
            e = tyokuzen.pop()
            q.append(e)
            root.append(e+1)

        


