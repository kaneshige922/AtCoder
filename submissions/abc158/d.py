from collections import deque


s = deque(list(input()))
q = int(input())

t = True

for i in range(q):
    qu = list(input().split())
    if int(qu[0]) == 1:
        t = not(t)
    else:
        if t:
            if int(qu[1]) == 1:
                s.appendleft(qu[2])
            else:
                s.append(qu[2])
        else:
            if int(qu[1]) == 1:
                s.append(qu[2])
            else:
                s.appendleft(qu[2])

s = list(s)

if not(t):
    s.reverse()

print("".join(s))
