from collections import deque
import math

n,h = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]

a = [i[0] for i in ab]
b = [i[1] for i in ab]
a.sort(reverse=True)
b.sort(reverse=True)
a = deque(a)
b = deque(b)

cnt = 0

while h > 0:
    if b and  a[0] < b[0]:
        d = b.popleft()
        h -= d
        cnt += 1
    else:
        cnt += math.ceil(h/a[0])
        h -= a[0]*math.ceil(h/a[0])

print(cnt)
