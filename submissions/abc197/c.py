from collections import deque

n = int(input())
a = list(map(int,input().split()))

ans = 2**30

for i in range(2**(n-1)):
    k = deque()
    k.append(a[0])
    for j in range(n-1):
        if (i>>j) & 1:
            k.append(a[j+1])
        else:
            u = k.pop()
            k.append(u | a[j+1])
    s = k.popleft()
    while k:
        s = s^k.popleft()
    ans = min(ans,s)

print(ans)

