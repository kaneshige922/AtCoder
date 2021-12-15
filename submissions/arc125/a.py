n,m = map(int,input().split())
a = list(map(int,input().split()))
t = list(map(int,input().split()))
k = -1
if a[0] == 1:
    for i in range(1,n):
        if a[i] == 0 or a[-i] == 0:
            k = i
            break
else:
    for i in range(1,n):
        if a[i] == 1 or a[-i] == 1:
            k = i
            break

h = a[0]
s = False
ans=0
for i in range(m):
    if t[i] == h:
        ans += 1
    else:
        if s:
            ans += 2
            h = t[i]
        else:
            if k == -1:
                print(-1)
                exit()
            else:
                ans += k+1
                h = t[i]
                s = True

print(ans)
