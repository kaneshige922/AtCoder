from collections import deque

n =int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a = deque(sorted(a))
b = deque(sorted(b))
c = deque(sorted(c))

ans = 0

for i in range(2*n):
    if not(a) or not(b) or not(c):
        break
    if a[0] < b[0]:
        if b[0] < c[0]:
            d = a.popleft()
            e = b.popleft()
            f = c.popleft()
            ans += 1
        else:
            c.popleft()
    else:
        b.popleft()


print(ans)
            

