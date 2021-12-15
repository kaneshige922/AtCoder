from collections import deque

n,m = map(int,input().split())
k = [list(map(int,input().split())) for i in range(m)]
p = list(map(int,input().split()))

ans = 0

for i in range(2**n):
    s = deque()
    cnt = 0
    for j in range(n):
        if (i>>j) & 1:
            s.append(1)
        else:
            s.append(0)
    for j in range(m):
        guuki = 0
        for l in range(k[j][0]):
            if s[k[j][l+1]-1] == 1:
                guuki += 1
        if guuki % 2 == p[j]:
            cnt += 1
    if cnt == m:
        ans += 1 

print(ans)
