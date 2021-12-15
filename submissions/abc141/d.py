from collections import deque

n,m = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse=True)

a = deque(a)
b = deque()
if n == 1:
    for i in range(m):
            a[0] //= 2
    print(a[0])
    exit()
elif n == 2:
    for i in range(m):
        a[0] //= 2
        if a[0] < a[1]:
            h = a.popleft()
            a.append(h)
    print(sum(a))
    exit()

for i in range(m):
    a[0] //= 2
    if len(a) >= 2:
        if a[0] < a[1]:
            h = a.popleft()
            if b:
                if b[0] < h:
                    b.appendleft(h)
                else:
                    b.append(h)
                if a:
                    if a[0] < b[0]:
                        h = b.popleft()
                        a.appendleft(h)
            else:
                b.append(h)
            if len(a) == 1:
                h = b.popleft()
                if h > a[0]:
                    a.appendleft(h)
                else:
                    a.append(h)
        elif b:
            if a[0] < b[0]:
                h = a.popleft()                
                s = b.popleft()
                a.appendleft(s)
                if b:
                    if b[0] < h:
                        b.appendleft(h)
                    else:
                        b.append(h)
                else:
                    b.append(h)

ans = a + b


print(sum(a+b))
