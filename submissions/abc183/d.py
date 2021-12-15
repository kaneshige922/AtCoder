n,w = map(int,input().split())
stp = [list(map(int,input().split())) for i in range(n)]

t = [stp[i][1] for i in range(n)]

mt = max(t)

a = [0]*(mt+1)

for i in stp:
    a[i[0]] += i[2]
    a[i[1]] -= i[2]

for i in range(1,mt+1):
    a[i] = a[i] + a[i-1]

if max(a) > w:
    print("No")
else:
    print("Yes")


