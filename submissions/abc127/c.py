n,m = map(int,input().split())
l = []
r = []
for i in range(m):
    a,b = map(int,input().split())
    l.append(a)
    r.append(b)

lm = max(l)
rm = min(r)

ans = rm-lm+1
if ans > 0:
    print(ans)
else:
    print(0)
