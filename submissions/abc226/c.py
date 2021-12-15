from collections import deque

n = int(input())

tka = [list(map(int,input().split())) for i in range(n)]


ans = tka[n-1][0]
v = set([n-1])
queue = deque([n-1])

while(queue):
    h = queue.popleft()
    for i in range(tka[h][1]):
        to = tka[h][2+i]-1
        if to not in v:
            ans += tka[to][0]
            v.add(to)
            queue.append(to)

print(ans)
