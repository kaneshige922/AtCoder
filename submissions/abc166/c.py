n,m = map(int,input().split())
h = list(map(int,input().split()))
r = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    r[b-1].append(a-1)
    r[a-1].append(b-1)

ans = 0

for i in range(n):
    t = True
    for j in r[i]:
        if i != j:
            if h[i] <= h[j]:
                t = False
                break
    if t:
        ans += 1

print(ans)
